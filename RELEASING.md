# Release workflow

- `develop` automatically deploys only to the dedicated `*-dev` EdgeOne project.
- Production EdgeOne projects follow `main` only. Never push directly to `main`.
- Cut `release/rel_1.0` (or the next release) from the tested develop commit. Freeze feature work there; apply only release fixes and merge them back to develop.
- Verify the candidate on Dev and record both web/API source commits, physical-device results, compatible app versions and a rollback target in the release PR.
- Open `release/rel_*` -> `main` PRs. Merge after verification and review. Merging starts the production build and deployment.
- After successful production smoke checks, create an immutable `v1.0.0` tag on the deployed main commit in each repository. Record the web/API commits and EdgeOne deployment IDs together. Never move a published version tag.
- Keep `release.json` version accurate before cutting the release branch. `/version.json` reports version, exact commit, branch, environment and build time; API also serves `/api/version`.
- Roll back to a recorded successful deployment, then revert the change through a new PR. Never rewrite production history.

## Environment mapping

| Purpose | Web project / URL | API project / URL | Branch |
| --- | --- | --- | --- |
| Dev | bee-trainer-web-dev.edgeone.dev | bee-trainer-api-dev.edgeone.dev | develop |
| Production | bee-trainer-web.edgeone.dev | bee-trainer-api.edgeone.dev | main |

Set `BEE_DEPLOY_ENV=development` on Dev projects and `BEE_DEPLOY_ENV=production` on production projects. Do not set a fixed commit SHA; builds obtain it from the checked-out Git repository. The Dev projects use their own primary deployment slot (called Production by EdgeOne); they are still development services, separate from the live projects. Other branches are not connected to live traffic.

Blob namespaces belong to their project. Dev and Production API projects therefore have distinct `bee-trainer-shares` stores. Never put an operator token into the app, web config or build metadata. Dev remote config must point to the Dev API, and production config must point to the Production API.

## iOS device verification

Use the default Xcode scheme Run / Debug: `Bee Trainer Dev`, bundle ID `com.beetrainer.mobile.dev`, Dev remote-config URL. It installs alongside the App Store app, with separate sandbox data. Archive / Release retains `Bee Trainer`, bundle ID `com.beetrainer.mobile`, and Production remote config. Do not select Release for ordinary on-device Run, because matching bundle IDs replace the installed app.

Check version endpoints and release config, share/redeem, old-code compatibility, and paywall cancellation on Dev before opening the production PR. A simulator pass does not replace physical-device background upload or StoreKit validation.

## GitHub enforcement

The public web repository protects `main` with required PRs, the `validate` CI check, up-to-date branches and resolved conversations. Administrator bypass, force pushes and branch deletion are disabled. Because this is a solo maintainer workflow, there is no separate approving-review quorum; the maintainer reviews and merges the PR after verification.

The API repository remains private on GitHub Free. The owner explicitly chose to retain Free and use the same PR/CI/release process without technical branch-protection enforcement for this private repository. Do not claim direct main pushes are blocked there. Never publish the repository or purchase a plan automatically.
