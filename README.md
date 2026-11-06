# Legacy — site

The landing page, privacy policy and support page for the Legacy iPhone app, served by GitHub
Pages from `main` at the repo root: https://peterbarnett03.github.io/legacy/

The privacy policy here is the one App Store Connect points at. It describes what the app in
`../LegacySwift` actually does; change the app, then change the page, and update the "Last
updated" date.

## Screenshots

Not hand-made. `tools/process-shots.py` resizes and re-encodes the frames the app repo's
`AppStoreScreenshots` UI test captures on the simulator (`docs/app-store/screenshots/6.9-inch/` there).
Nothing is retouched: if something in one of these looks wrong, it is wrong in the app.

    ./tools/process-shots.py      # 330px and 660px WebP into shots/ (needs Pillow)

## Local preview

    python3 -m http.server 8000
