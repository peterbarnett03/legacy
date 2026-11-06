# CLAUDE.md

## What this is

The marketing, privacy and support site for the Legacy iPhone app, served by GitHub Pages from
`main` at the repo root. Hand-written files — `index.html`, `privacy.html`, `support.html`,
`style.css` — plus generated screenshots in `shots/`. No build step, no framework, no CDN, no
JavaScript. `.nojekyll` disables Jekyll processing; pushing to `main` publishes.

## Commands

```sh
python3 -m http.server 8000   # local preview
./tools/process-shots.py      # regenerate shots/ from the app repo's screenshots (needs Pillow)
```

There are no tests. Verifying a change means loading the three pages at both widths (narrow and
>860px) and in both colour schemes.

## The app repo is the source of truth

The sibling checkout `../LegacySwift` owns everything this site describes.

- **Privacy policy.** App Store Connect points at `privacy.html`. It must describe what the app
  does: what is collected (see `LegacySwift/PrivacyInfo.xcprivacy` and the App Privacy answers in
  `docs/app-store/metadata.md` there), who processes it (Firebase, OpenAI via Cloud Functions),
  and how deletion works (Settings → Account → Delete account calls `deleteMyData`). Change the
  app, then the page, and bump "Last updated".
- **Colours.** `style.css` takes its palette from `LegacySwift/Theme/AppColors.swift`.
- **Screenshots.** Captured by the `AppStoreScreenshots` UI test in the app repo, signed in as the
  App Review demo account. `tools/process-shots.py` only resizes and re-encodes.

Claims on `index.html` and `support.html` (one question a day, "Ask me something else", family
access, Print or share, offline-safe uploads) are product claims. Check them against the app
before writing new ones.
