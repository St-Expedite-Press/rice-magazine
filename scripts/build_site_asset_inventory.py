"""Build the inventory for standalone RICE site media.

Run from the repository root:
    python scripts/build_site_asset_inventory.py
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "site-assets.json"

ASSETS = {
    "archive-ledger.jpg": ("archive-document", ["archive.html", "archive-template.html", "poetry.html"]),
    "archive-placeholder.png": ("fallback-texture", []),
    "feature-archive.png": ("section-feature", ["index.html", "archive.html"]),
    "feature-essays.jpg": ("section-feature", ["index.html", "essays.html"]),
    "feature-fiction.jpg": ("section-feature", ["index.html", "fiction.html"]),
    "feature-poetry.jpg": ("section-feature", ["index.html", "poetry.html"]),
    "feature.png": ("general-feature", ["essays.html", "poetry.html", "archive.html"]),
    "issue-specimen.jpg": ("publication-specimen", ["archive.html", "shop.html"]),
    "logo.png": ("site-identity", ["all HTML pages"]),
    "noise.png": ("surface-texture", ["styles.css"]),
    "rice-field-loop.mp4": ("splash-background-video", ["splash.html"]),
    "rice_field.png": ("splash-poster-and-feature", ["splash.html", "styles.css", "section pages"]),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build() -> None:
    image_root = ROOT / "images"
    actual = {path.name for path in image_root.iterdir() if path.is_file()}
    expected = set(ASSETS)
    if actual != expected:
        missing = sorted(expected - actual)
        unmanaged = sorted(actual - expected)
        raise RuntimeError(f"Site asset inventory mismatch; missing={missing}, unmanaged={unmanaged}")

    records = []
    for filename, (role, used_by) in ASSETS.items():
        path = image_root / filename
        record = {
            "id": f"RICE-SITE-{path.stem.upper().replace('-', '_')}",
            "path": path.relative_to(ROOT).as_posix(),
            "role": role,
            "used_by": used_by,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        if path.suffix.lower() != ".mp4":
            with Image.open(path) as image:
                image = ImageOps.exif_transpose(image)
                record["width"] = image.width
                record["height"] = image.height
                record["format"] = image.format
        else:
            record["format"] = "MP4"
        records.append(record)

    inventory = {
        "schema_version": 1,
        "generated": date.today().isoformat(),
        "scope": "Standalone site media in images/; editorial collection assets are cataloged separately.",
        "source_of_truth": "images/",
        "assets": records,
    }
    OUTPUT.write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(records)} site assets at {OUTPUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    build()
