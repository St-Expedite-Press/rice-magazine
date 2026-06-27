"""Canonical RICE asset categories.

A coarse routing layer that sits *above* the per-inventory role/family
taxonomy. Every catalogued asset — editorial or standalone — carries exactly
one ``category`` slug drawn from :data:`CATEGORIES`.

This module is the single source of truth. Both build scripts and the
validator import it; the asset-library browser reads the emitted ``categories``
block, so the four-plus-one scheme is defined in exactly one place.
"""

from __future__ import annotations

# Ordered intentionally: the four content categories first, system last.
CATEGORIES = {
    "archive": "Reusable archival imagery for archive image slots anywhere on the site.",
    "article": "Imagery bound directly to a single article, essay, poem, or fiction piece.",
    "feature": "Imagery bound to a site element such as a section landing, shop, or submissions.",
    "photo": "Standalone photography or photo-submission carousels.",
    "system": "Site chrome and identity media: logo, textures, splash, and fallbacks.",
}

# The categories that describe published editorial/content imagery.
CONTENT_CATEGORIES = ("archive", "article", "feature", "photo")

# File extensions the inventories treat as managed media. Companion files such
# as AGENTS.md, MEMORY.md, and README.md live alongside images but are not assets.
MEDIA_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".mp4", ".webm"}


def is_media(path) -> bool:
    """True if ``path`` is a managed media file (by extension)."""
    return path.is_file() and path.suffix.lower() in MEDIA_SUFFIXES


def category_block() -> list[dict]:
    """Return the serialisable category definitions for an inventory file."""
    return [{"id": slug, "description": description} for slug, description in CATEGORIES.items()]


def validate_category(category: str, label: str) -> None:
    """Raise if ``category`` is not one of the canonical slugs."""
    if category not in CATEGORIES:
        raise ValueError(
            f"{label}: unknown asset category {category!r}; "
            f"expected one of {', '.join(CATEGORIES)}"
        )
