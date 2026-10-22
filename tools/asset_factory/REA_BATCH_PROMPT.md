# REA Agent Prompt: Independent Product Rebuild

## Mission

Investigate a selected candidate from `tools/asset_factory/catalog.json` and build a genuinely useful independent Kreovant product. The goal is a repeatable asset business, not cosmetic rebranding.

## Hard gates

1. Inspect the exact upstream license text and all bundled assets, fonts, icons, images, JS/CSS libraries and dependencies.
2. If a license is missing or unclear, stop implementation that relies on the source and mark `BLOCKED_RIGHTS`. Do not assume publicly available means reusable.
3. If copyleft terms apply, explain the obligations and distribution implications; do not proceed to commercial packaging until reviewed.
4. Preserve notices required by applicable licenses. Do not erase upstream author attribution from third-party material where retention is required.
5. Do not use REA to bypass access controls, DRM, authentication, payment, anti-bot systems or other technical restrictions. Analyze only sources and applications you are authorized to examine.
6. Do not copy branding, marketing text, product screenshots, customer data, paid assets or original demo imagery into the new product.
7. If the candidate's license permits independent reimplementation but not redistribution of its code/assets, use functional observations and independently write new code without copying expressive source material. If legal status is uncertain, stop and request review.

## Required workflow

### A. Establish evidence
- Record candidate ID, source URL, commit/version, acquisition date and SHA-256 of downloaded archive/source license.
- Use REA where applicable to map website structure, interactive states, route behavior, visible workflows and JavaScript module relationships.
- Keep evidence distinct from assumptions. Add screenshots or tool outputs only when actually captured.
- For source repositories, inspect the actual code, package scripts, dependencies, assets and build process. REA is complementary, not a replacement for code review.

### B. License and asset audit
- Read the full license, not only the repository badge.
- Inventory external dependencies and their licenses.
- Inventory image, font, icon and illustration sources.
- Mark status as `PASS`, `REVIEW`, or `BLOCKED`, with reasons and links.
- Do not build or publish from a blocked candidate.

### C. Define a meaningful improvement
Choose a specific customer and problem. Examples:
- resume/portfolio: print-ready CV, case-study layouts, keyboard navigation, reduced-motion support;
- agency template: service detail pages, case studies, accessible contact flow;
- landing page: real form validation, pricing comparison, FAQ, mobile-first layout;
- dashboard: responsive tables, empty/error states, accessible data visualization.
Define acceptance tests before coding.

### D. Implement independently
- Use Kreovant's own design system: pale grey `#e8e9ee`, near-black `#111216`, acid lime `#d5ff36` as an accent.
- Write original structure, styles, scripts, content, assets and component naming. Do not copy whole source files and then run a rename operation.
- Avoid unnecessary external runtime calls. Use local original assets and system fonts unless a licensed dependency materially improves the product.
- Add responsive layouts, semantic HTML, keyboard-visible focus, reduced-motion handling where animation exists, sensible SEO metadata and clear placeholder labels.
- Do not invent customer testimonials, performance claims, integrations or payment behavior.

### E. Test and package
- Run the repository's relevant lint, build and test commands. Add tests where the project has none.
- Test at narrow and wide viewports; check console errors, links, forms, accessibility basics, print mode where applicable, and offline/no-third-party-request behavior.
- Create `README.md`, `CHANGELOG.md`, `THIRD_PARTY_NOTICES.md`, `QA_REPORT.md`.
- Record commands actually executed and actual outcomes. No guessed pass status.

### F. Report
Update `tools/asset_factory/reports/product-ledger.json` with:
- candidate ID, upstream commit, license status, bundled asset audit;
- independent implementation path, features added, tests run and results;
- blockers, remaining manual review and release readiness.

Do not publish or charge for the product. Stop at a release candidate and report the exact files changed.
