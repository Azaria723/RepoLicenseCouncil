# Cloudflare Pages production verification

- Production URL: [https://repo-license-council.pages.dev/](https://repo-license-council.pages.dev/)
- Immutable deployment URL: [https://32881b10.repo-license-council.pages.dev/](https://32881b10.repo-license-council.pages.dev/)
- Cloudflare Pages project: `repo-license-council`, production branch `master`.
- Production page: HTTP `200`.
- Logo `/logo.png`: HTTP `200`.
- Served JavaScript bundle: `/assets/index-CdT_LF6c.js`.
- Served bundle contains the configured contract `0xfEa116bEa66ba7FF6F7Cc4573c949a22f2Fc1665` and StudioNet Explorer links. Public [transaction evidence](studionet-verification.md) remains in the repository, not the frontend navigation.

The frontend reads authoritative council and case state from the deployed GenLayer contract. Its evidence links point to the exact GitHub commit revisions bound in each case.
