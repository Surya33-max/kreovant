# REA-powered Asset Re-engineering: Batch Runbook

This is the agent brief for the Kreovant Asset Factory. Use REA as an investigation tool, then have the coding agent build independent implementations in this repository. Do not treat REA output as permission to copy or redistribute source.

## Objective

Turn the 20-entry asset shortlist into a pipeline that produces independently implemented, improved Kreovant products. The first batch currently has 13 Git-based website templates in `tools/asset_factory/catalog.json`; seven UI-kit entries need their exact download URLs and license text recorded before automated acquisition can include them.

## Setup

1. Install Node.js 22.19+ or a supported current Node.js version and Git.
2. From a local clone of `Surya33-max/kreovant`, run:

   ```bash
   npx rea-agents@latest setup
   ```

3. Select the coding agent you actually use, approve the proposed config changes, and restart it. Keep the existing config backed up.
4. Confirm REA tools are available to the agent. REA can inspect website behavior and JavaScript/Electron apps; its deeper native analysis needs separately installed analysis providers.
5. Run the acquisition/audit script, then review every report before asking the agent to implement a product.

Official REA project: https://github.com/morluto/rea
Official setup: https://rea.tools/
REA is MIT licensed for REA-authored code; third-party source and assets retain their own licenses.

## Agent execution prompt

Paste this into your REA-connected coding agent from the repository root:

> Read `tools/asset_factory/REA_BATCH_PROMPT.md`, `tools/asset_factory/catalog.json`, and the latest audit report. Use REA's available analysis tools where they provide evidence about the source application's structure or behavior. Work on one candidate at a time. Never remove required notices or bypass license restrictions. Do not treat source screenshots or copied demo assets as reusable. For each candidate, produce an evidence-backed feature map, a third-party asset inventory, and a license decision before writing code. Then implement an original Kreovant product in its own `products/<slug>/` directory, using independent markup, styling, component structure, content and code. Use the source only as a functional reference to the extent permitted. Add a meaningful improvement, responsive behavior, accessibility, print/install instructions as relevant, and tests. Run all available checks. If a license is absent, unclear, copyleft obligations are unresolved, or an asset's provenance is unknown, stop that candidate and continue to the next one. Do not publish or create a sales listing automatically. Update `tools/asset_factory/reports/product-ledger.json` with status and evidence. At the end, report exactly what was changed, commands run, test results, unresolved risks and output paths.

## Batch discipline

- Limit each run to 1–3 products, not all 20 at once. This keeps context, tests, and review manageable.
- Run REA analysis on the target application or original website when useful; use source-code inspection and build/test tools for source repositories.
- Treat screenshots and runtime observations as evidence, not as a license.
- Use original CSS, original content and original UI composition; replace remote fonts, image URLs and third-party assets unless reuse is explicitly permitted.
- Preserve required upstream license notices in a product's `THIRD_PARTY_NOTICES.md`. Keep a clean-room implementation record if the original source is not copied.
- Never claim a product is tested unless the commands were actually run. Never mark a license as cleared based on filename alone.
- A human must approve legal status, final build and marketplace listing.

## Output contract per candidate

```
products/<slug>/
  index.html or src/
  README.md
  CHANGELOG.md
  THIRD_PARTY_NOTICES.md
  QA_REPORT.md
  package.json (when needed)
tools/asset_factory/reports/<id>-research.md
tools/asset_factory/reports/product-ledger.json
```

The output is an original, maintained product, not a repackaged upstream download.
