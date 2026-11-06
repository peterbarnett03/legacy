#!/usr/bin/env python3
"""Turns the app's App Store screenshots into web assets.

    ./tools/process-shots.py [source-directory]

Source defaults to `../LegacySwift/docs/app-store/screenshots`, which is what the app repo's
`AppStoreScreenshots` UI test writes (1320x2868 PNGs from the iPhone 18 Pro Max simulator).
Nothing here retouches the app's pixels: frames are resized and re-encoded, and that is all. If
something in one of these looks wrong, it is wrong in the app; fix it there and recapture.

Two widths per shot (1x and 2x for a column around 320 CSS pixels wide), WebP at quality 82, so
the whole set stays small for someone opening the privacy policy on a phone.
"""

import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = ROOT.parent / "LegacySwift" / "docs" / "app-store" / "screenshots" / "6.9-inch"
OUT = ROOT / "shots"

WANTED = {
    "1-today.png": "today",
    "2-recording.png": "recording",
    "3-book.png": "book",
    "4-chapter.png": "chapter",
}
WIDTHS = (330, 660)

def main() -> int:
    source = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    OUT.mkdir(exist_ok=True)
    for name, web in WANTED.items():
        path = source / name
        if not path.exists():
            print(f"missing {path}", file=sys.stderr)
            return 1
        with Image.open(path) as im:
            im = im.convert("RGB")
            for width in WIDTHS:
                height = round(im.height * width / im.width)
                out = OUT / (f"{web}.webp" if width == WIDTHS[0] else f"{web}@2x.webp")
                im.resize((width, height), Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
                print(f"{out.name}: {width}x{height} {out.stat().st_size // 1024} KB")
    return 0

if __name__ == "__main__":
    sys.exit(main())
