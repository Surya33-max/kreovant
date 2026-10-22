# Kreovant Asset Factory

Automates repetitive source acquisition and license triage for the asset-flip workflow. It does not silently remove attribution, overwrite third-party branding, or auto-publish source.

## Requirements

- Python 3.10+
- Git installed and available on PATH

## Run

From the repository root:

```bash
python3 tools/asset_factory/asset_pipeline.py
```

Only run selected assets:

```bash
python3 tools/asset_factory/asset_pipeline.py --ids resume agency
```

Refresh clones from upstream:

```bash
python3 tools/asset_factory/asset_pipeline.py --refresh
```

Create review stubs for candidates with a provisional permissive-license signal:

```bash
python3 tools/asset_factory/asset_pipeline.py --allow-stage
```

## Outputs

- `tools/asset_factory/downloads/<id>/`: source clone for inspection. Never publish directly.
- `tools/asset_factory/reports/latest-audit.json`: machine-readable audit.
- `tools/asset_factory/reports/latest-audit.md`: human-readable summary.
- `tools/asset_factory/reports/staging/<id>/SOURCE_REVIEW_REQUIRED.md`: review queue.

## Important behavior

- Missing license is blocked.
- Copyleft or unclear license signals require review.
- A detected MIT license is only provisional, not final clearance.
- Dependencies, images, fonts, icons, screenshots, and marketplace rules need separate review.
- The script records the upstream commit and hashes license files.
- It never removes license files or attribution.
- It does not pretend a generic code rewrite can be safely automated without understanding the target product. Build original implementations in `products/`, test them, and package only after rights/QA approval.

## Batch cycle

1. Run acquisition and triage.
2. Review provisional candidates and blocked items.
3. Pick one product with a clear user problem.
4. Build the Kreovant implementation in its own folder under `products/`.
5. Run tests, check external requests, inspect bundled assets and add a changelog.
6. Package, list and record real metrics.
