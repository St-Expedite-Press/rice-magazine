# RICE Asset Library

The asset library separates editorial images into three delivery tiers and records their provenance in one generated catalog.

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

## Workflow

1. Put an approved source image in its city’s `master/` folder.
2. Add or update its prompt record in `docs/city-image-prompts.json`.
3. Run `python scripts/build_asset_library.py`.
4. Review `asset-library.html` through a local web server.
5. Reference the `web` path in site pages; reserve `master` for print or reprocessing.

Generated archival imagery must always retain its disclosure and must never be represented as an authenticated historical record.
