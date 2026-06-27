# RICE Magazine

## Agent framework

- `AGENTS.md` defines repository behavior, validation, secrets, and closeout rules.
- `ONTOLOGY.md` maps source ownership, generated files, update coupling, and validation commands.
- `MEMORY.md` records durable project changes, checks, follow-ups, and tooling notes.
- Local `AGENTS.md` and `MEMORY.md` files exist under `assets/`, `assets/images/`, `docs/`, and `scripts/` for scoped work.

Every file-changing task should update the relevant memory file and assess whether scripts, tooling, skills, or ontology need to change.

RICE is an independent literary magazine of essays, fiction, poetry, and archival work from the Gulf South. This repository contains the magazine’s static website and the design system for its first volume.

![RICE splash page over a rice field at golden hour](docs/screenshots/splash-desktop.png)

## About

RICE is a Southern literary magazine informed by post-alt-lit, C86 zine culture, and retro modernist aesthetics.

Rooted in New Orleans, RICE publishes essays, fiction and poetry by writers who explore the unique texture of the Gulf South while looking outward to broader cultures and movements.

We believe that literary publications should be both severe and welcoming: our pages are spare but alive with thought. We value work that resists nostalgia, embraces the present moment, and experiments with form.

Founded by [St. Expedite Press](https://stexpedite.press), RICE functions as a broadsheet companion to our more devotional and archival projects.

## The project

The site treats the web edition as a piece of printed matter: a strict editorial grid, heavy grotesque masthead, serif reading typography, monospace metadata, photocopied grain, and restrained black rules. New Orleans coordinates run through the identity as a quiet geographic colophon.

The splash page pairs a distressed paper panel with an ambient, image-generated rice-field loop. The main issue expands into oversized section indexes, asymmetric reading pages, marginal notes, pull quotes, a freeform poetry stage, a filterable archive, a submission call sheet, a manifesto, and a physical-edition specimen.

The design is intentionally lightweight and framework-free. It uses semantic HTML, a shared stylesheet, and a small dependency-free interaction layer for issue search, archive filters, image zoom, and reading mode. Responsive layouts, keyboard focus states, reduced-motion support, and poster-image fallback remain built in.

## Screens

| Desktop issue page | Mobile splash |
| --- | --- |
| ![RICE Volume 1 homepage on desktop](docs/screenshots/home-desktop.png) | ![RICE splash page on mobile](docs/screenshots/splash-mobile.png) |

### Mobile issue page

![RICE Volume 1 homepage on mobile](docs/screenshots/home-mobile.png)

### Editorial system

| Essay index | Reading page |
| --- | --- |
| ![RICE essay section index](docs/screenshots/essays-index.png) | ![RICE essay reading page](docs/screenshots/essay-reading.png) |

| Archive index | Physical issue specimen |
| --- | --- |
| ![RICE archive contact sheet](docs/screenshots/archive-index.png) | ![RICE Volume 1 shop specimen](docs/screenshots/shop-specimen.png) |

## Site structure

- `splash.html` — ambient entrance page with preorder and submission actions
- `index.html` — Volume 1 cover and table of contents
- `essays.html`, `fiction.html`, `poetry.html` — section landing pages
- `essay-template.html`, `fiction-template.html`, `poem-template.html` — editorial templates
- `archive.html`, `archive-template.html` — archival material and field-card format
- `about.html`, `submissions.html`, `shop.html` — magazine information and calls to action
- `styles.css` — shared visual system and responsive behavior
- `site.js` — search (built from `assets/articles.json`), reading mode, archive filters, random archive slots, zoom, and form states
- [`docs/IMAGE_STYLE_GUIDE.md`](docs/IMAGE_STYLE_GUIDE.md) — C86 × South × St. Expedite Press image direction, prompt presets, and archive ethics

Additional image direction: [`docs/CITY_IMAGE_PROMPTS.md`](docs/CITY_IMAGE_PROMPTS.md) contains five tightly constrained image families for five Southern bohemian cities.

## Data model

RICE treats every image and every editorial work as a **typed, validated asset
with a single source of truth**. The model has two classification axes, one shared
geographic field, and a set of JSON inventories that the site reads at build time
and at runtime. The canonical definitions live in
[`scripts/asset_categories.py`](scripts/asset_categories.py); the full reference is
[`docs/ASSET_SCHEMA.md`](docs/ASSET_SCHEMA.md).

### Two taxonomies

The word *category* means two different things depending on what is being classified,
so the model keeps them as separate enumerations:

| Axis | Applies to | Values | Answers |
| --- | --- | --- | --- |
| **Image category** (`CATEGORIES`) | every image | `archive`, `article`, `feature`, `photo`, `system` | *Where may this image be placed?* (which slot / pool) |
| **Work category** (`ARTICLE_CATEGORIES`) | every article/work | `article`, `fiction`, `poetry`, `photo`, `archive` | *What kind of work is this?* (content type) |

They share some labels (`article`, `photo`, `archive`) but are deliberately distinct:
an image's category routes its placement, while a work's category names its content.

### `place` — the shared field

`place` is the one geographic field used on both sides. Images carry
`place`/`place_slug` (formerly `city`/`city_slug`); works carry `place` (formerly the
informal "parish"). Same name, one concept.

### Inventories

| File | Holds | Source |
| --- | --- | --- |
| [`assets/catalog.json`](assets/catalog.json) | Editorial image collection — accession id, title, `place`, `category`, role/family, orientation, rights, provenance, AI disclosure, prompt lineage, caption, tags, and `web`/`master` files with dimensions + SHA-256 | Generated from masters + prompt manifest |
| [`assets/site-assets.json`](assets/site-assets.json) | Standalone runtime media (logo, textures, feature covers, ledger) — id, path, `category`, role, consumers, size/checksum, and `place`/caption/tags where relevant | Generated |
| [`assets/image-pools.json`](assets/image-pools.json) | Runtime pools for randomizable categories (`archive`, `photo`): `src`, `alt`, `caption`, `tags`, `focal_point` | Generated from the two inventories |
| [`assets/photo-slots.json`](assets/photo-slots.json) | Every rendered image slot — page, location, `category`, image, caption, and `random`/`pool` for shuffling slots | Hand-authored |
| [`assets/articles.json`](assets/articles.json) | Editorial **works** — `id`, `title`, `category` (work type), `place`, `author`, `date`, `description`, `keywords`, `ref`, `href`, `hero` | Hand-authored |

`articles.json` is the source of truth for works: `site.js` builds the search index
from it rather than from a hardcoded list.

### On-disk layout

Images are organized **only by category** — the served web rendition of each image
lives in its category folder, with originals kept out of the rendered set:

```text
assets/
  images/   archive/ article/ feature/ photo/ system/   # one web rendition each
  masters/  archive/ article/ _incoming/                 # originals, not referenced by the site
```

### Build & validate

Masters and standalone files are the inputs; everything else is generated and checked:

```sh
python scripts/build_asset_library.py        # masters -> catalog.json + web renditions
python scripts/build_site_asset_inventory.py # standalone media -> site-assets.json
python scripts/build_image_pools.py          # inventories -> image-pools.json
python scripts/check_assets.py               # validate everything (see below)
```

`check_assets.py` enforces the model end to end: known categories, no orphan served
files, every slot's image matching its category, random slots pointing at a non-empty
pool, and each work's category/required fields/`href`/`hero` resolving. Inventories are
also documented in [`assets/README.md`](assets/README.md), and the editorial collection
is browsable at `asset-library.html`.

## Local preview

Serve the repository with any static web server:

```sh
python -m http.server 4173
```

Then open:

- `http://localhost:4173/splash.html`
- `http://localhost:4173/index.html`

## Publisher

[St. Expedite Press](https://stexpedite.press) · New Orleans, Louisiana  
29.9511° N, 90.0715° W
## Agent framework

- `AGENTS.md` defines repository behavior, validation, secrets, and closeout rules.
- `ONTOLOGY.md` maps source ownership, generated files, update coupling, and validation commands.
- `MEMORY.md` records durable project changes, checks, follow-ups, and tooling notes.
- Local `AGENTS.md` and `MEMORY.md` files exist under `assets/`, `assets/images/`, `docs/`, and `scripts/` for scoped work.

Every file-changing task should update the relevant memory file and assess whether scripts, tooling, skills, or ontology need to change.
