# RICE Asset Management

RICE has two deliberately separate inventories:

- `catalog.json` records accessioned editorial collections, provenance, prompts, and delivery tiers.
- `site-assets.json` records standalone runtime media such as the logo, noise texture, splash video, poster, and section features.

## Categories

Every asset in both inventories carries one `category` — a coarse routing layer
above the `role`/`family` taxonomy:

- `archive` — reusable imagery for archive slots anywhere on the site.
- `article` — imagery bound to a single article, essay, poem, or fiction piece.
- `feature` — imagery bound to a site element such as a section landing, shop, or submissions.
- `photo` — standalone photography or photo-submission carousels (reserved).
- `system` — site chrome and identity media (logo, textures, splash, fallbacks).

The categories are defined once in [`../scripts/asset_categories.py`](../scripts/asset_categories.py);
see [`../docs/ASSET_SCHEMA.md`](../docs/ASSET_SCHEMA.md) for the full mapping and rules.

## Directory system

Images are assets. They live under `assets/`, and the only sub-directories of
the served image root are the five categories:

```text
assets/
  images/
    archive/   article/   feature/   photo/   system/   # served web renditions (≤1800 px)
  masters/
    archive/   article/   _incoming/                     # original masters, not referenced by the site
  catalog.json        site-assets.json
  photo-slots.json    image-pools.json
  articles.json
```

Images carry `place`/`place_slug` (renamed from `city`/`city_slug`); articles carry
`place` (was the informal "parish"). One shared geographic field.

One web rendition per image (no thumb tier). Do not edit served files by hand —
they are regenerated from `assets/masters/<category>/`. Standalone media are
placed directly in their category folder.

## Stable IDs

```text
RICE-CFN-NOL-SFN-001
     │   │   │   └── sequence
     │   │   └────── role code
     │   └────────── city code
     └────────────── collection code
```

City codes: `NOL`, `ATH`, `AVL`, `SAV`, `RIC`.

Role codes:

- `SFN` — street field note
- `WIN` — working interior
- `ARC` — archival evidence
- `POR` — maker portrait
- `NOC` — nocturnal aftermath

## Editorial fields

Every entry in [`catalog.json`](catalog.json) includes:

- stable accession ID;
- place, role, family, category, orientation, and approval status;
- `web` and `master` paths with dimensions and file size;
- alt text, responsive focal point, caption, and tags;
- rights, provenance, model, generation date, and AI disclosure;
- the production prompt and its source manifest.
- SHA-256 checksums for the web rendition and master.

Every entry in [`site-assets.json`](site-assets.json) includes a stable ID, category, role, known consumers, dimensions where applicable, byte size, and SHA-256 checksum (plus caption/tags for archive-pool members).

[`image-pools.json`](image-pools.json) is generated from both inventories: it lists the randomizable-category images (`archive`, `photo`) with `src`, `alt`, `caption`, `tags`, and `focal_point`, and is fetched at runtime by `site.js` to fill random slots.

[`articles.json`](articles.json) is the hand-authored **work data model** (`id`, `title`, `category` [article/fiction/poetry/photo/archive], `place`, `author`, `date`, `description`, `keywords`, `ref`, `href`, `hero`). `site.js` builds the search index from it; `check_assets.py` validates it. See [`../docs/ASSET_SCHEMA.md`](../docs/ASSET_SCHEMA.md).

## Workflow

1. Put an approved editorial master in `assets/masters/<category>/` (category = its role's category).
2. Add or update its prompt record in `docs/city-image-prompts.json`.
3. Run `python scripts/build_asset_library.py` (writes the web rendition to `assets/images/<category>/`).
4. If a standalone file changed, place it in `assets/images/<category>/` and update `scripts/build_site_asset_inventory.py`, then run it.
5. Run `python scripts/build_image_pools.py`, then `python scripts/check_assets.py`.
6. Review `asset-library.html` through a local web server.
7. Reference the `assets/images/<category>/` web path in pages; reserve masters for print or reprocessing.

Do not add an unmanaged media file under `assets/images/`: editorial files come from the master pipeline, and standalone files must be declared in `scripts/build_site_asset_inventory.py`. `check_assets.py` fails on any orphan served file.

Generated archival imagery must always retain its disclosure and must never be represented as an authenticated historical record.
