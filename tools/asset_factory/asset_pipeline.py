#!/usr/bin/env python3
"""Kreovant Asset Factory: acquire sources, audit rights, and stage a review report.

This tool deliberately does not strip attribution, remove license files, or publish
third-party code automatically. It creates a repeatable acquisition/audit queue.
Use --allow-stage only for repositories whose license and bundled assets were
reviewed by a human. Original Kreovant implementations belong in products/.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tools" / "asset_factory"
CATALOG = BASE / "catalog.json"
DOWNLOADS = BASE / "downloads"
REPORTS = BASE / "reports"
# Permissive signals only. Presence of a license is not full clearance.
SAFE_SIGNALS = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "CC0-1.0"}
LICENSE_NAMES = ("LICENSE", "LICENCE", "COPYING", "UNLICENSE")

def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=False)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def license_files(repo: Path) -> list[Path]:
    found = []
    for p in repo.rglob("*"):
        if not p.is_file() or p.name.upper() not in LICENSE_NAMES:
            continue
        if any(part in {".git", "node_modules", "vendor", "dist", "build"} for part in p.parts):
            continue
        found.append(p)
    return found

def classify_license(files: list[Path], expected: str) -> tuple[str, str]:
    if not files:
        return "BLOCKED", "No license file found; public visibility does not grant reuse rights."
    text = "\n".join(p.read_text(errors="ignore")[:100000] for p in files).lower()
    if "gnu general public license" in text or "gpl-" in text:
        return "REVIEW", "Copyleft license detected; obligations and distribution model need specialist review."
    if "mozilla public license" in text or "creative commons attribution" in text:
        return "REVIEW", "Additional license-specific obligations require review."
    if expected not in SAFE_SIGNALS:
        return "REVIEW", f"Catalog expected license '{expected}' is not on the permissive allowlist."
    if expected == "MIT" and "permission is hereby granted" in text:
        return "PROVISIONAL", "MIT-like text detected. Preserve notice; audit dependencies, fonts, images and marketplace terms."
    if expected == "Apache-2.0" and "apache license" in text:
        return "PROVISIONAL", "Apache license detected. Preserve notices and check NOTICE/patent requirements."
    if expected in {"BSD-2-Clause", "BSD-3-Clause", "ISC", "CC0-1.0"}:
        return "REVIEW", "License family needs exact SPDX identification and notice review before staging."
    return "REVIEW", "License text did not confidently match the catalog signal."

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*", help="Only process these catalog IDs")
    ap.add_argument("--refresh", action="store_true", help="Fetch latest source; otherwise keep existing clone")
    ap.add_argument("--allow-stage", action="store_true", help="Copy provisional candidates to review staging (never auto-publish)")
    args = ap.parse_args()
    items = json.loads(CATALOG.read_text())
    if args.ids:
        items = [x for x in items if x["id"] in args.ids]
        missing = set(args.ids) - {x["id"] for x in items}
        if missing:
            ap.error("Unknown IDs: " + ", ".join(sorted(missing)))
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    results = []
    for item in items:
        dest = DOWNLOADS / item["id"]
        if dest.exists() and args.refresh:
            shutil.rmtree(dest)
        if not dest.exists():
            print(f"[ACQUIRE] {item['id']} <- {item['source']}")
            proc = run(["git", "clone", "--depth", "1", item["source"], str(dest)])
            if proc.returncode:
                results.append({**item, "status":"ERROR", "detail":proc.stdout[-1500:]})
                continue
        rev = run(["git", "rev-parse", "HEAD"], cwd=dest)
        commit = rev.stdout.strip() if rev.returncode == 0 else "unknown"
        licenses = license_files(dest)
        status, detail = classify_license(licenses, item.get("license_expected", ""))
        hashes = {str(p.relative_to(dest)): sha256_file(p) for p in licenses}
        # Any common bundled-asset folders are flagged for manual inventory.
        asset_dirs = [str(p.relative_to(dest)) for p in dest.iterdir()
                      if p.is_dir() and p.name.lower() in {"assets", "img", "images", "fonts", "icons", "vendor"}]
        if status == "PROVISIONAL":
            detail += " This is not final clearance; review every dependency and bundled asset."
        if args.allow_stage and status == "PROVISIONAL":
            stage = REPORTS / "staging" / item["id"]
            stage.mkdir(parents=True, exist_ok=True)
            (stage / "SOURCE_REVIEW_REQUIRED.md").write_text(
                f"# Review required: {item['name']}\n\n"
                f"Upstream: {item['source']}\nCommit: {commit}\n"
                f"License status: {status}\n\n{detail}\n\n"
                "Do not sell this source unchanged. Build a differentiated product and preserve required notices.\n"
            )
        results.append({**item, "status":status, "detail":detail, "commit":commit,
                        "license_files":[str(p.relative_to(dest)) for p in licenses],
                        "license_sha256":hashes, "asset_dirs_to_review":asset_dirs})
        print(f"[{status}] {item['id']}: {detail}")
    report = {"generated_at":datetime.now(timezone.utc).isoformat(),
              "policy":"No automatic license stripping or publishing; human review required.",
              "results":results}
    out = REPORTS / "latest-audit.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    md = ["# Kreovant Asset Factory Audit", "", f"Generated: {report['generated_at']}", "",
          "> This report is a triage aid, not legal clearance. Never remove required notices.", "",
          "| Asset | Status | Source commit | License files | Details |", "|---|---|---|---|---|"]
    for x in results:
        md.append(f"| {x['name']} | **{x['status']}** | `{x.get('commit','n/a')}` | "
                  f"{', '.join(x.get('license_files', [])) or 'none'} | {x.get('detail','').replace('|','/')} |")
    (REPORTS / "latest-audit.md").write_text("\n".join(md) + "\n")
    print(f"\nReports written: {out.relative_to(ROOT)} and {(REPORTS / 'latest-audit.md').relative_to(ROOT)}")
    print("Next: review each license and bundled asset, then implement original Kreovant code in products/.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
