# RICE Asset Management

RICE has two deliberately separate inventories:

- `catalog.json` records accessioned editorial collections, provenance, prompts, and delivery tiers.
- `site-assets.json` records standalone runtime media such as the logo, noise texture, splash video, poster, and section features.

## Directory system

```text
images/editorial/
  city-field-notes/
    <city>/
      master/  original approved generation
      web/     publication-ready JPEG, maximum 1800 px
      thumb/   browser and contact-sheet JPEG, maximum 640 px
```

Do not edit files in `web/` or `thumb/` by hand. Rebuild them from the masters.

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
- city, role, family, orientation, and approval status;
- master, web, and thumbnail paths with dimensions and file size;
- alt text and responsive focal point;
- rights, provenance, model, generation date, and AI disclosure;
- the production prompt and its source manifest.
- SHA-256 checksums for every master and derivative.

Every entry in [`site-assets.json`](site-assets.json) includes a stable ID, role, known consumers, dimensions where applicable, byte size, and SHA-256 checksum.

## Workflow

1. Put an approved source image in its city’s `master/` folder.
2. Add or update its prompt record in `docs/city-image-prompts.json`.
3. Run `python scripts/build_asset_library.py`.
4. If a standalone file under `images/` changed, run `python scripts/build_site_asset_inventory.py`.
5. Run `python scripts/check_assets.py`.
6. Review `asset-library.html` through a local web server.
7. Reference the `web` path in site pages; reserve `master` for print or reprocessing.

Do not add an untracked file directly under `images/`: add its ownership metadata to `scripts/build_site_asset_inventory.py`, rebuild the inventory, and check it. Editorial collection files belong under `images/editorial/`, not in the standalone inventory.

Generated archival imagery must always retain its disclosure and must never be represented as an authenticated historical record.
