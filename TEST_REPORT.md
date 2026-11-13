# November 5, 2026 content validation

- Public support mailbox `beetrainer.studio@gmail.com` is linked consistently across Support, Terms and both privacy pages. The checker permits mailto and informational HTTPS anchors while continuing to reject external runtime dependencies.
- Updated all five HTML pages. English and Simplified Chinese privacy policies retain matching sections and technical claims. Public operator, contact and effective date are filled; no CONFIRM/确认 placeholders remain in HTML.
- `python3 scripts/check_site.py`: PASS for metadata, local links/fragments, reciprocal language links, local CSS and both version JSON contracts.
- Browser inspection: desktop landing rendering, Support navigation and expandable backup FAQ passed. At a 390 × 844 mobile viewport, all five pages had no horizontal overflow; landing and Chinese privacy screenshots were visually inspected. No cross-browser or real-device claim is made.
- Live EdgeOne landing, English privacy, Support, Terms and iOS JSON returned successfully before edits. These checks describe the existing deployed draft, not publication of this change.
- The iOS release contract remains schema 1 with both versions at `0.0.0`, an empty Store URL and disabled future feature flags. These are intentional pre-release values until a real published listing exists.
- Outstanding: real host and support-email retention/region review; final App Store audience/privacy answers; deployment verification after merging to owner-confirmed `develop`. Sylvia and the support mailbox are owner-confirmed, and policy effective date is November 5, 2026. Do not treat this content update as App Store approval.

---

## Historical validation

# Local validation report

Executed October 13, 2026 on `feature/static-website`.

## Passed

- `python3 scripts/check_site.py`: five HTML pages; language, title, description metadata; internal files and fragment targets; reciprocal English/Chinese policy links; local CSS; both version JSON contracts, types, and numeric version ordering.
- Live Python static-server requests: landing, both policies, support, terms, CSS, and both JSON files returned HTTP 200. HTML/CSS/JSON MIME types were correct, including `application/json` on both configuration routes.
- Headless Chromium via the environment's existing Playwright installation: all five pages displayed at desktop 1440×1100 and mobile 390×844 viewports with no horizontal overflow or page errors. Privacy language switching, FAQ expansion, and keyboard skip-to-content worked.
- Desktop/mobile landing screenshots visually inspected: responsive columns, readable text, navigation and footer, no clipping.
- All runtime resources are local; no JavaScript, external fonts, trackers, API requests, secrets, or credential configuration were introduced. Placeholder scans reviewed; all unconfirmed details are explicitly documented in README.

The initial standalone Chromium screenshot command failed because its default profile directory was unwritable. Playwright used a writable temporary profile and completed the browser checks without installing dependencies.

## Outstanding before production

- Owner-approved developer identity, support email, policy effective dates, actual app features/data flows, children's privacy details, and legal review. English/Chinese policy equivalence must be preserved when replacing placeholders.
- Actual published iOS/Android versions and store URLs. `0.0.0` is a documented pre-release sentinel; confirm client handling before using it.
- Native configuration caching, update comparison/dialogs, fail-open startup behavior, and disabled defaults: outside website scope and untested.
- Tencent account/GitHub integration, deployment, automatic main-branch builds, deployed directory paths, JSON MIME/cache headers, HTTPS, free-plan limits, and mainland China/Canadian network reachability: untested. No remote push or deployment occurred.
- Safari, Edge, real mobile devices, assistive technology, and full accessibility audit: untested. Chromium checks do not establish cross-browser certification.

The local website development workflow is verified. Production release remains blocked by the items above.
