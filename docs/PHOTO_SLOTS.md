# RICE Photo Slot Map

Every rendered image/media slot on the site, the asset **category** it draws from,
and its caption metadata. The machine-readable source of truth is
[`../assets/photo-slots.json`](../assets/photo-slots.json); category definitions live
in [`../scripts/asset_categories.py`](../scripts/asset_categories.py) and are explained
in [`ASSET_SCHEMA.md`](ASSET_SCHEMA.md).

`scripts/check_assets.py` validates this manifest: every slot's image must exist and
its asset category must equal the slot's assigned category, so a slot can never silently
drift to a wrong-category image.

Images live in `assets/images/<category>/`; the image names below are the basenames
in those folders. **Archive slots randomize**: the four archive grid cards are marked
`data-random="archive"` and `site.js` fills them with random images from the archive
pool ([`../assets/image-pools.json`](../assets/image-pools.json)) on each load, with the
caption following the drawn image. Their listed image/caption is the no-JS fallback.

## How slots are categorized

| Category | Slots that draw from it |
|---|---|
| `feature` | Promotional feature strips (index issue strip, section landing strips) and the shop specimen. |
| `archive` | Archive index grid, archive feature strip, archive record scans, and archival inserts embedded in a piece. |
| `article` | Figures embedded in a single reading piece that depict that piece. |
| `photo` | Standalone photography / photo-submission carousels. **No slots yet — reserved.** |
| `system` | Site chrome: splash media, favicon, surface textures. Never captioned. |

Captions render as **Title / Byline / Series**; an empty byline or series collapses
that segment. Slots marked “—” have no rendered caption (chrome or alt-only images).

## feature (17 slots)

| Slot | Page | Image | Links to | Caption |
|---|---|---|---|---|
| index-feature-01 | index.html | feature-essays.jpg | essay-template | **Crowley Modernism** / C. Sandbatch / Essay 01 |
| index-feature-02 | index.html | feature-fiction.jpg | fiction-template | **The Pump House** / L. Doucet / Fiction 03 |
| index-feature-03 | index.html | feature-poetry.jpg | poem-template | **Crawfish Pond with Saints** / C. Sandbatch / Poetry 04 |
| index-feature-04 | index.html | feature-archive.png | archive-template | **Mill Ledger, 1911** / Archive / RC-ACD-1911-004 |
| essays-feature-01 | essays.html | feature-essays.jpg | essay-template | **Crowley Modernism** / C. Sandbatch / Essay 01 |
| essays-feature-02 | essays.html | feature-archive.png | essay-template | **Against Cotton Memory** / J. T. Miller / Essay 02 |
| essays-feature-03 | essays.html | feature.png | archive-template | **A Field Guide to Damp Heat** / RICE Editors / Field Note |
| poetry-feature-01 | poetry.html | feature-poetry.jpg | poem-template | **Crawfish Pond with Saints** / C. Sandbatch / Poem 04 |
| poetry-feature-02 | poetry.html | feature-archive.png | poem-template | **Three Rice Songs** / M. Lapointe / Sequence |
| poetry-feature-03 | poetry.html | feature.png | poem-template | **Mosquito Litany** / J. T. Miller / 28 Lines |
| fiction-feature-01 | fiction.html | feature-fiction.jpg | fiction-template | **The Pump House** / L. Doucet / Fiction 03 |
| fiction-feature-02 | fiction.html | feature.png | fiction-template | **Twenty-Six Hours of Fluorescent Light** / M. Lapointe |
| fiction-feature-03 | fiction.html | feature-archive.png | fiction-template | **Parish Line** / A. Guidry / Fiction 05 |
| archive-feature-01 | archive.html | feature-archive.png | archive-template | **Mill Ledger, 1911** / RC-ACD-1911-004 |
| archive-feature-02 | archive.html | feature.png | archive-template | **Field at 19:42** / RC-FLD-2026-017 |
| archive-feature-03 | archive.html | issue-specimen.jpg | shop | **Volume 1 Specimen** / RC-PUB-2026-001 |
| shop-specimen | shop.html | issue-specimen.jpg | — | — (alt only) |

## archive (6 slots)

| Slot | Page | Image | Links to | Caption |
|---|---|---|---|---|
| archive-card-01 | archive.html | archive-ledger.jpg | archive-template | **Mill Ledger, 1911** / RC-ACD-1911-004 / Acadia Parish / Ledger |
| archive-card-02 | archive.html | new-orleans-street-field-note.jpg | archive-template | **Field at 19:42** / RC-FLD-2026-017 / Weather / Photograph |
| archive-card-03 | archive.html | athens-archival-evidence.jpg | archive-template | **Damp Heat Index** / RC-WTH-2026-009 / Survey / Chart |
| archive-card-04 | archive.html | archive-ledger.jpg | archive-template | **Shipper / Weight / Grade** / RC-ACD-1911-004B / Detail / Ledger |
| archive-record-scan | archive-template.html | archive-ledger.jpg | — | **Mill Ledger, 1911** / Acadia Parish / RC-ACD-1911-004 |
| essay-document-insert | essay-template.html | new-orleans-archival-evidence.jpg | — | **Document insert 01** / drainage records and map fragments / RICE visual reconstruction |

`archive-card-01`…`-04` are **random** (`data-random="archive"`, pool `archive`, 11
images); the rows above show their static fallback. `archive-record-scan` (bound to a
record) and `essay-document-insert` (bound to the essay) stay fixed.

`essay-document-insert` is an archive-category image embedded inside an essay — the
intended use of `archive` assets, which may fill archive slots anywhere on the site.

## article (1 slot)

| Slot | Page | Image | Links to | Caption |
|---|---|---|---|---|
| fiction-full-bleed | fiction-template.html | new-orleans-nocturnal-aftermath.jpg | — | **Night shift** / evidence of recent use / New Orleans field note |

## system (4 slots)

| Slot | Page | Image | Caption |
|---|---|---|---|
| splash-video | splash.html | rice-field-loop.mp4 (poster rice_field.png) | — |
| splash-backdrop | splash.html | rice_field.png (CSS background) | — |
| site-texture | all pages | noise.png (CSS texture) | — |
| site-favicon | all pages | logo.png | — |

## photo (0 slots)

Reserved. When photo submissions arrive, add their carousel/standalone slots here with
`category: "photo"` and the submission imagery in the catalog.

## Re-pointing log (2026-06-27)

Seven slots were drawing a wrong-category image and were re-pointed so each slot matches
its category:

| Slot | Was | Now | Reason |
|---|---|---|---|
| essays-feature-02 | rice_field.png (system) | feature-archive.png | system image in a feature strip |
| poetry-feature-02 | archive-ledger.jpg (archive) | feature-archive.png | archive image in a feature strip |
| fiction-feature-02 | rice_field.png (system) | feature.png | system image in a feature strip |
| fiction-feature-03 | archive-ledger.jpg (archive) | feature-archive.png | archive image in a feature strip |
| archive-feature-02 | rice_field.png (system) | feature.png | system image in a feature strip |
| archive-card-02 | rice_field.png (system) | new-orleans-street-field-note.jpg | system image in an archive card |
| archive-card-03 | feature.png (feature) | athens-archival-evidence.jpg | feature image in an archive card |

## Adding or changing a slot

1. Edit the HTML, then mirror the change in `assets/photo-slots.json` (image, category, caption).
2. Fixed slot: the `category` must equal the image's asset category (see `catalog.json` / `site-assets.json`). Random slot: set `"random": true` and `"pool": "<category>"`, mark the element `data-random="<category>"`, and keep a category-correct static fallback image.
3. Run `python scripts/build_image_pools.py` (if pools changed), then `python scripts/check_assets.py` — it fails on unknown categories, missing images, category mismatches, orphan files, or empty random pools.
