# Bee Trainer website

Static landing, English/Simplified Chinese privacy, support, terms, and public native-app version configuration. Plain UTF-8 HTML and shared CSS; no JavaScript, build, npm packages, backend, tracking, or externally loaded assets.

## Local development

Use the existing isolated checkout; no worktree is needed. Changes belong on `feature/*` branches (current implementation: `feature/static-website`). Review locally, then open a PR from `feature/*` into `develop`. Review that PR before merging. A separate reviewed promotion PR from `develop` into `main` controls production release. No Tencent deployment has been performed.

With Python 3 installed, from this repository:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 0.0.0.0
```

Open the local server in your own development browser. Stop it with Ctrl-C. This server is for development only. No installation or build command is required. Pages use relative links and directory indexes, including under a hosting path prefix.

## Routes

- `/` — landing
- `/privacy/` — English policy
- `/privacy/zh/` — Simplified Chinese policy
- `/support/` — support
- `/terms/` — terms
- `/config/v1/ios.json` and `/config/v1/android.json` — stable version endpoints

## Tencent EdgeOne Pages (Makers)

Deployment is not yet configured or verified. In Tencent's current Pages console:

1. Select the free/Makers plan and check current quotas, eligibility, available deployment regions, and free subdomain terms. Do not enable paid options inadvertently.
2. Create a Pages project, connect GitHub through Tencent's authorized integration, and select `auston-d/bee-trainer-web`.
3. Select `main` as the production branch and automatic deployments on changes merged into `main`. Keep this feature branch out of production until owner review. Preview branches, if enabled, must be reviewed for public exposure of draft policies.
4. Choose the static/no-framework option. Leave install/build commands empty and set the published output directory to the repository root (`.`), according to the console's current controls. No server runtime or functions are needed.
5. Use the generated free project subdomain and enable/verify HTTPS. A custom domain can be configured later; internal links do not depend on the provider hostname.
6. After deployment, request every route directly (including nested directory indexes), test all links on desktop/mobile, and confirm both JSON endpoints return status 200 and `Content-Type: application/json` over HTTPS. Check for SPA rewrites, authentication, or HTML error pages that could break JSON.
7. Configure JSON caching through EdgeOne's supported project/CDN controls if needed. Use a short TTL or revalidation for version endpoints, and verify actual response headers and cache invalidation. Do not assume local Python headers describe EdgeOne behavior. Redeploy website/config changes and verify the public JSON before relying on it.

Exact console labels and plan details may change; confirm them in Tencent's current documentation. GitHub integration authorization and Tencent project creation must be performed by the owner. No deployment account credentials are needed for local development.

### China accessibility

All runtime resources are local and system fonts are used. This does **not** establish mainland China reachability. Confirm the deployment region, free-subdomain access limitations, and Tencent's current custom-domain requirements. Mainland delivery with a custom domain may require ICP filing and other provider/regional prerequisites; a free offshore subdomain does not guarantee reliable mainland access. Do not purchase a domain or file ICP as part of this MVP. Test HTTPS pages and JSON from real mainland networks and Canadian networks before treating them as production-critical. Neither production HTTPS nor China reachability has been tested here.

## Remote configuration contract

Both JSON files contain the same schema (version 1):

```json
{
  "schemaVersion": 1,
  "latestVersion": "0.0.0",
  "minimumSupportedVersion": "0.0.0",
  "updateMessage": "",
  "storeUrl": "",
  "features": {
    "wordAssociation": false,
    "imageGeneration": false
  }
}
```

`0.0.0` is an explicit **pre-release sentinel**, not a claim that any app version is published. Both store URLs are empty and all feature flags are disabled. The native clients must agree to this sentinel or these files must remain unused until real release values are supplied. Before production, set `latestVersion` to the newest **published** version, `minimumSupportedVersion` to the lowest permitted version (no higher than latest), a relevant update message, and the platform's actual store listing. Android remains unadvertised until release.

For example, after a confirmed iOS 1.2.0 release, latest could be `1.2.0` and minimum `1.0.0` if versions 1.0.0 and later remain supported. Do not copy this example as a release claim. Native apps compare numeric semantic-style version components, never lexical strings. Build numbers or prerelease suffixes require an agreed client convention; these files currently use three numeric components only.

Native apps determine optional/mandatory upgrades, cache the last valid configuration, handle invalid responses, and default missing/invalid feature flags to disabled. An unreachable endpoint must not block startup solely because retrieval failed. Client logic is outside this repository. Updates here require a website deployment, but no mobile app rebuild. Never put secrets in public configuration, change existing field names/types, or delete/rename endpoints without a migration plan. Add future versions under new paths if incompatible schema changes are necessary.

## Release-blocking placeholders

Search all HTML for `CONFIRM`, `确认`, and `pending`, and review this checklist before production:

- Replace `[CONFIRM SUPPORT EMAIL]` throughout support, English privacy, and terms, and `[确认支持邮箱]` in Chinese privacy. Contact text on the landing page also requires replacement. Contact is deliberately plain text until a real address exists; add matching `mailto:` links if desired. Search all occurrences instead of changing only one page.
- Supply the real developer/legal name and effective dates; do not invent company details.
- Confirm actual released features, basic usage controls, progress support, languages, offline behavior, and intended age group. Landing features are explicitly planned, not advertised as available.
- Verify microphone/audio/transcript flows, recognition provider, vocabulary/progress storage and backups, data categories, third-party SDKs, sharing, retention, deletion, security, international processing, and child/parental protections against app code and App Store disclosures.
- Confirm hosting request logs and remote-config request metadata. Keep English and Chinese policies equivalent after every edit.
- Obtain owner/legal review of terms, age/license rules, intellectual property, purchase/refund/subscription rules if applicable, consumer rights, jurisdiction, and notification mechanisms.
- Replace the App Store availability badge with a real download link only after approval. Do not add an Android download link until available.
- Replace version sentinels and verify native-client behavior, public JSON MIME types, caching, HTTPS, and real mainland reachability.

The HTML policies are marked drafts. Local implementation readiness is not legal approval or production release readiness.

## Validation

`python3 scripts/check_site.py` checks HTML language/title/description metadata, local file links and fragments, absence of external runtime resources, bilingual policy links, and JSON fields/types/version ordering. It uses only Python's standard library. Browser rendering, live HTTP status/MIME tests, and deployed-provider checks are separate; see `TEST_REPORT.md` for executed results and limitations.
