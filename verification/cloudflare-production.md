# Cloudflare Pages production verification

- Production URL: [https://repo-license-council.pages.dev/](https://repo-license-council.pages.dev/)
- Immutable deployment URL: [https://715a3214.repo-license-council.pages.dev/](https://715a3214.repo-license-council.pages.dev/)
- Cloudflare Pages project: `repo-license-council`, production branch `master`.
- Production page: HTTP `200`.
- Logo `/logo.png`: HTTP `200`.
- Served JavaScript bundle: `/assets/index-TRO8Lkej.js`.
- Served bundle contains the configured contract `0xfEa116bEa66ba7FF6F7Cc4573c949a22f2Fc1665`, StudioNet Explorer links, and the public [transaction evidence](studionet-verification.md).

The frontend reads authoritative council and case state from the deployed GenLayer contract. Its evidence links point to the exact GitHub commit revisions bound in each case.
