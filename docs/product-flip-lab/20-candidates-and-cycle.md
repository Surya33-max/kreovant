# Kreovant Product Flip Lab: 20-Asset Discovery Cycle
_Last reviewed: 2026-10-22 · Status: discovery shortlist, not yet cleared for release_

## Goal

Find existing small tools that can be legally improved into a genuinely more useful Kreovant product. This is not a plan to scrape and relabel other people's work. The value must come from measurable improvements, better packaging, workflow integration, documentation, compatibility, or a focused audience.

## Rules before touching source

1. **No license, no fork for commercial use.** A public GitHub repository is not a license. Candidates marked "No license" below are research-only until permission is granted.
2. Read the upstream LICENSE file and any marketplace terms before copying, modifying, redistributing, or charging.
3. Preserve copyright, license, and attribution notices required by the license. Track dependencies and their separate licenses.
4. Do not copy logos, product names, screenshots, premium assets, fonts, or customer data without permission. Rebrand only our original additions and only where permitted.
5. An MIT/Apache/CC0 label is an initial signal, not final legal clearance. Check the current upstream repository and dependencies immediately before use.
6. Figma Community listing rules and third-party API rules still apply. Upstream source being open does not guarantee that a fork can be published under any name or monetized in any way.
7. Never sell a cosmetic rebrand. A candidate needs a user-visible improvement and a basic QA record before launch.

## Shortlist: 20 candidates

License labels below reflect the Figma community-resources index at research time; re-open the upstream license before selecting one. "Commercial path" means a possible path after review, not legal approval.

| # | Candidate / source | What it does | Potential improvement worth testing | License signal | Initial call |
|---:|---|---|---|---|---|
| 1 | [Polychrom](https://github.com/evilmartians/figma-polychrom) | Contrast checking, APCA guidance, color conversions | Batch audit report, exportable remediation checklist, clearer team handoff | MIT | **A: investigate** |
| 2 | [Chroma](https://github.com/kaleidocode-app/chroma) | Creates color styles in bulk | Safer token naming, duplicate detection, preview/undo workflow | MIT | **A: investigate** |
| 3 | [Dominant Color Toolkit](https://github.com/brianlovin/figma-dominant-color-toolkit) | Builds palettes from images | Palette accessibility checks, semantic roles, export formats | MIT | **B: investigate** |
| 4 | [Easing Gradient](https://github.com/alexwidua/figma-easing-gradients) | Generates smoother gradient stops | Presets, repeatable controls, design-token export | MIT | **B: investigate** |
| 5 | [Lucidi](https://github.com/dimuuu/lucidi) | Syncs opacity styles from base color styles | Better variable-mode support and conflict warnings | CC0 | **B: investigate** |
| 6 | [Design Lint](https://github.com/destefanis/design-lint) | Finds design inconsistencies | Focused rulesets, report export, fix prioritization | MIT | **A: investigate** |
| 7 | [Design Tokens](https://github.com/lukasoppermann/design-tokens) | Exports design tokens | DTCG validation, presets for web/iOS/Android, robust error messages | MIT | **A: investigate** |
| 8 | [Styler](https://github.com/andreincu/Styler) | Helps build and maintain design systems | Batch operations, preview/diff, safer rollback | MIT | **B: investigate** |
| 9 | [Themer](https://github.com/thomas-lowry/themer) | Swaps styles from published libraries | Theme mapping, missing-style diagnostics, team workflow docs | MIT | **B: investigate** |
| 10 | [Figma to Bootstrap 5](https://github.com/gabrielrbarbosa/figma-to-bootstrap-plugin) | Converts designs into Bootstrap snippets | Bootstrap 5.3 output, semantic markup, component-level export | GPL-3.0 | **C: copyleft review first** |
| 11 | [Tailwind CSS Figma plugin](https://github.com/ecklf/tailwindcss-figma-plugin) | Generates styles from Tailwind config | Tailwind v4 support audit, variable mapping, config diagnostics | MIT | **A: investigate** |
| 12 | [Android Resources Export](https://github.com/Ashung/android-resources-export-figma) | Exports assets into Android resource folders | Modern density presets, naming validation, batch export report | MIT | **B: investigate** |
| 13 | [Figma Format](https://github.com/kawamurakazushi/figma-format) | Groups canvas items by names | Custom naming rules, preview changes, non-destructive sorting | MIT | **A: investigate** |
| 14 | [GridGen](https://github.com/gnawx/figma-plugins/tree/master/packages/figma-gridgen) | Generates tables from native Figma layers | Table presets, editable data import, responsive table layouts | MIT (index points to shared repo license) | **A: investigate** |
| 15 | [Super Tidy](https://github.com/basiclines/figma-super-tidy) | Aligns, renames, and reorders frames | Custom rules, dry-run preview, undo-safe batch cleanup | MIT | **A: investigate** |
| 16 | [Better Font Picker](https://github.com/yenargy/figma-better-font-picker) | Previews fonts while choosing | Font pairing boards, missing-font checks, specimen export | MIT | **B: investigate** |
| 17 | [Content Buddy](https://github.com/basiclines/figma-content-buddy) | Replaces text across layers | CSV import/export, variable placeholders, validation before replace | MIT | **A: investigate** |
| 18 | [Batch Styler](https://github.com/six7/figma-batch-styler) | Edits multiple styles at once | Preview diffs, selective rollback, bulk variable support | MIT | **A: investigate** |
| 19 | [Figma Sort It](https://github.com/kawamurakazushi/figma-sort-it) | Sorts frames/layers by name or position | Saved sorting profiles and clearer non-destructive preview | MIT | **B: investigate** |
| 20 | [Variables Import](https://github.com/microsoft/figma-variables-import) | Imports design tokens as Figma variables | Better DTCG diagnostics, import preview, migration report | MIT | **A: investigate** |

### Discovery source

The main source is [Figma's community-resources plugin index](https://github.com/figma/community-resources/blob/main/plugins/README.md). It lists open-source plugins and starter resources, with per-project source and license links. The index itself explicitly asks users to perform due diligence and security review. We are using it as a discovery map, not as blanket permission.

## First-pass ranking

Scores are provisional hypotheses (1–5), not sales forecasts. "Ease" 5 means a small initial improvement looks feasible. "Rights" 5 means the index shows a permissive license signal; final clearance is still mandatory.

| Candidate | User pain | Improvement room | Ease | Rights signal | Total /20 |
|---|---:|---:|---:|---:|---:|
| Content Buddy | 4 | 5 | 4 | 4 | 17 |
| Super Tidy | 4 | 4 | 4 | 4 | 16 |
| Figma Format | 3 | 4 | 5 | 4 | 16 |
| Polychrom | 5 | 4 | 3 | 4 | 16 |
| Design Lint | 5 | 4 | 3 | 4 | 16 |
| Batch Styler | 4 | 4 | 3 | 4 | 15 |
| Chroma | 4 | 4 | 3 | 4 | 15 |
| Design Tokens | 5 | 4 | 2 | 4 | 15 |
| Tailwind CSS Figma plugin | 4 | 4 | 3 | 4 | 15 |
| GridGen | 3 | 4 | 4 | 4 | 15 |

**First build to validate:** Content Buddy, with CSV-backed bulk text replacement, preview-before-apply, and a clear rollback/test workflow. It is small enough to inspect, has an obvious workflow improvement, and can be tested with a demo file. Do not commit to it until upstream activity, dependencies, current Figma API compatibility, and license are checked.

## The repeating 14-day cycle

Each cycle ends with a decision: ship a verified improvement, publish a free lead magnet, or archive the candidate. "Publish" means release only after rights and QA gates pass.

| Day | Stage | Work | Exit criteria |
|---:|---|---|---|
| 1 | Discover | Add 5–10 candidates; record problem, upstream URL, activity, license, competitors | Candidate has a real user problem and working source link |
| 2 | Rights gate | Read LICENSE, dependency licenses, marketplace terms, assets/fonts terms | PASS / NEEDS REVIEW / BLOCKED recorded; no unknowns silently treated as permission |
| 3 | Demand check | Search reviews/issues/feature requests; inspect competing products and pricing | At least 3 concrete pain signals or mark demand unproven |
| 4 | Pick one | Score pain, improvement room, effort, competition, rights, support burden | One candidate wins; scope limited to a 2–4 day improvement |
| 5–7 | Improve | Fork/branch, make a distinct improvement, add settings/docs, keep attribution | A visible user outcome beyond branding |
| 8 | Test | Run tests, test in actual host app, test edge cases, verify clean install | QA checklist passes or blockers are documented |
| 9 | Package | README, changelog, screenshots/demo, install guide, license notices, privacy note | A stranger can install and understand it |
| 10 | Listing | Write honest marketplace/site copy, pricing hypothesis, support policy | No unsupported claims; asset ownership and license notices are correct |
| 11 | Publish gate | Recheck rights, dependencies, security, host marketplace rules | Human review of all blockers; publish only if all pass |
| 12 | Launch | Release to website/marketplace, post demo, collect feedback | Live listing URL and release tag recorded |
| 13 | Measure | Track visits, clicks, installs, conversion, refunds, support issues | Baseline metrics logged; no invented revenue |
| 14 | Decide/reinvest | Keep, improve, bundle, or archive; use actual results to choose next cycle | Decision plus next-cycle backlog recorded |

### Non-negotiable release checklist

- [ ] Upstream source and commit hash recorded.
- [ ] License text saved with the project and notices preserved.
- [ ] All dependencies and bundled assets reviewed.
- [ ] No unlicensed source or "no license" project included.
- [ ] Original improvements documented in changelog.
- [ ] Unit/mocked tests pass where applicable.
- [ ] Tested inside the real target application, not just mocked APIs.
- [ ] Clean install tested on a fresh copy.
- [ ] Privacy/data handling and network calls documented.
- [ ] Screenshots are from the actual product and do not misrepresent features.
- [ ] Marketplace policy and name/trademark conflicts checked.
- [ ] Support contact, version, limitations, and refund terms are clear.
- [ ] Pricing validated with real users before adding paid complexity.

## Budget and pricing experiment

Keep the first cycle under ₹5,000 and avoid paid ads. Use existing free hosting, GitHub, and a free or low-cost checkout/marketplace where available. Initial pricing hypotheses for a focused add-on or workflow pack: ₹299–₹999 one-time, or free core plus a paid pack. These are experiments, not researched market rates. Do not charge for an unchanged fork simply because a repository permits redistribution; sell the improvement, support, workflow, and packaging.

## Cycle log

| Cycle | Candidate | Rights gate | Improvement shipped | QA status | Listing URL | Results | Decision |
|---|---|---|---|---|---|---|---|
| 01 | Content Buddy (provisional) | Pending | CSV import + preview + validation (proposed) | Not started | Not published | No data yet | Start rights and code review |

## Sources

- [Figma community-resources plugin index](https://github.com/figma/community-resources/blob/main/plugins/README.md) — source and license links for the Figma plugin shortlist.
- [Figma plugin samples](https://github.com/figma/plugin-samples) — official examples for implementation reference.
- [Figma: publish plugins to the Community](https://help.figma.com/hc/en-us/articles/360042293394) — publishing guidance; review current requirements before release.
- [Tailwind UI license example](https://github.com/rayGreycloud/salient-tailwindui-demo/blob/main/LICENSE.md) — example of how a paid asset license can allow end-product use but prohibit redistribution of the assets or derivatives separately. Do not assume all asset licenses work the same way.

_Last updated by the Kreovant discovery workflow. No candidate in this document has been fully audited, forked, tested, or published as a product yet._
