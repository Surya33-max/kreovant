# Kreovant Studio : product website

Responsive static storefront for Kreovant, an independent digital marketplace. The site uses a refined soft-neumorphic system with violet and mint accents.

## Preview
Run `python3 -m http.server 8000` from this directory and open `http://localhost:8000`.

## Design files
- `assets/brand/BRAND.md`: brand strategy, color rules, typography, layout, accessibility
- `assets/brand/brand-system.json`: machine-readable design tokens and metadata
- `assets/brand/tokens.css`: canonical CSS tokens and focus styling
- `assets/brand/kreovant-mark.svg`: vector mark and favicon master
- `assets/brand/kreovant-wordmark.svg`: vector wordmark lockup
- `assets/brand/kreovant-social-card.svg`: 1200×630 social preview artwork
- `assets/products/*.svg`: product artwork masters for the marketplace catalogue
- `css/style.css`: responsive site structure and components
- `js/main.js`: filters, search, mobile navigation and contact form behavior

## Product kit\n- `social-launch-kit.html`: public kit landing page with individual SVG downloads and a client-side ZIP bundle action.\n- `assets/kits/social-launch-kit/*.svg`: 12 editable social layout templates.\n- The full source ZIP is stored in the working ChatGPT Library under `/Projects/Kreovant_Social_Launch_Kit_v1.0.0.zip`.\n\n## Metadata and release checks
The title, description, Open Graph and Twitter metadata use Kreovant's marketplace positioning. The contact form opens an email draft. Confirm the live destination and domain before running paid campaigns. SVG social images may not render on every social crawler, so export a PNG fallback before launch.

Product status must stay explicit. The Social Launch Kit is available as individually downloadable SVG templates with a client-side ZIP bundle action. FrameFlow remains a local-testing prototype until it passes the Figma runtime QA checklist. Other catalogue concepts should not be represented as purchasable until delivery, pricing and product destinations exist.

## Reference
Reviewed Themesberg's open-source Neumorphism UI repository for general neumorphic patterns: https://github.com/technext/neumorphism-ui (MIT). Its vendor logos and artwork are not included in the Kreovant identity. If code is copied from that upstream project later, preserve the copyright and MIT license notice.
