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
The title, description, Open Graph and Twitter metadata use Kreovant's marketplace positioning. The contact form POSTs to the Python serverless function at `/api/contact`, which sends the enquiry via SMTP. Configure `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, and `CONTACT_TO` as Vercel Environment Variables before testing production email. The default destination is `suryalh44@gmail.com`. SVG social images may not render on every social crawler, so export a PNG fallback before launch.

Product status must stay explicit. The Social Launch Kit is available as individually downloadable SVG templates with a client-side ZIP bundle action. FrameFlow remains a local-testing prototype until it passes the Figma runtime QA checklist. Other catalogue concepts should not be represented as purchasable until delivery, pricing and product destinations exist.

## Reference
Reviewed Themesberg's open-source Neumorphism UI repository for general neumorphic patterns: https://github.com/technext/neumorphism-ui (MIT). Its vendor logos and artwork are not included in the Kreovant identity. If code is copied from that upstream project later, preserve the copyright and MIT license notice.


## Website contact email setup (Vercel)

The contact form sends from the website through `api/contact.py`; visitors do not need an email app.

1. In Vercel, open the project connected to this repository and go to **Settings → Environment Variables**.
2. Add the following variables for **Production** (and Preview if you want to test preview deployments):
   - `SMTP_HOST`: your email provider's SMTP server (for Gmail, `smtp.gmail.com`)
   - `SMTP_PORT`: `465` for SSL, or `587` for STARTTLS
   - `SMTP_USER`: the mailbox address used to send the enquiry notification
   - `SMTP_PASSWORD`: an SMTP/app password, never a normal account password where app passwords are supported
   - `CONTACT_TO`: destination inbox (defaults to `suryalh44@gmail.com`)
3. Save the variables and redeploy the project. Vercel does not expose secret values to the repository, so credentials must be added in the Vercel dashboard.
4. Submit the contact form on the deployed site and verify that the destination inbox receives the enquiry. Check Vercel Function Logs if delivery fails.

For Gmail, enable 2-Step Verification and create an App Password if your account supports it. Do not commit SMTP credentials to GitHub or place them in frontend JavaScript. The API validates input, limits request size, uses a honeypot field, and keeps SMTP credentials server-side.
