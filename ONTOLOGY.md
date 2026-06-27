# RICE Magazine Ontology

This file is the navigation contract for `rice_site/`. Read it after `AGENTS.md` and before selecting files to edit.

## Maintained Surfaces

| Surface | Source of truth | Notes |
|---|---|---|
| Page markup | Root `*.html` files | Static, framework-free pages. Preserve semantic HTML, keyboard focus, and reduced-motion behavior. |
| Shared visual system | `styles.css` | Single shared stylesheet for the magazine site. |
| Site behavior | `site.js` | Dependency-free interaction layer for reading/search/archive behavior. |
| Asset browser | `asset-library.html`, `asset-library.css`, `asset-library.js` | Internal browser for editorial image assets. |
| Asset metadata | `assets/catalog.json`, `assets/site-assets.json` | Generated or maintained inventories; do not hand-edit generated measurements. Each asset carries a `category` (`archive`/`article`/`feature`/`photo`/`system`). |
| Asset category schema | `docs/ASSET_SCHEMA.md`, `scripts/asset_categories.py` | Canonical category definitions and mapping. `asset_categories.py` is the single source of truth imported by both builders and the validator. |
| Photo-slot map | `assets/photo-slots.json`, `docs/PHOTO_SLOTS.md` | Every rendered image/media slot, the category it draws from, and its caption metadata. `check_assets.py` enforces that each slot's image category equals the slot's category. |
| Served images | `assets/images/<category>/` | One web rendition per image; the only sub-directories are the five categories. Generated for editorial; placed directly for standalone. |
| Image masters | `assets/masters/<category>/` | Original editorial masters (unreferenced by the site). `_incoming/` holds unpromoted candidates. |
| Runtime image pools | `assets/image-pools.json` | Generated: `category -> [{src, alt, caption, tags, focal_point}]` for randomizable categories (archive, photo). `site.js` fetches it to fill random slots. |
| Image doctrine and prompts | `docs/IMAGE_STYLE_GUIDE.md`, `docs/city-image-prompts.json`, `docs/CITY_IMAGE_PROMPTS.md` | Source for prompt style, provenance, and archive ethics. |
| Asset tooling | `scripts/build_asset_library.py`, `scripts/build_site_asset_inventory.py`, `scripts/build_image_pools.py`, `scripts/check_assets.py` | Rebuild inventories, web renditions, and pools through scripts. |

## Working Directories

| Directory | Owns | Local files |
|---|---|---|
| `assets/` | Inventories, served images (`images/<category>/`), masters, and pools | `AGENTS.md`, `MEMORY.md`, `README.md` |
| `assets/images/` | Served web renditions, one folder per category | `AGENTS.md`, `MEMORY.md` |
| `docs/` | Image doctrine, prompt docs, screenshots, contact sheets | `AGENTS.md`, `MEMORY.md` |
| `scripts/` | Python asset build/check scripts | `AGENTS.md`, `MEMORY.md` |

Root HTML, `styles.css`, `site.js`, and `asset-library.*` remain governed by the project-level `AGENTS.md` and this ontology.

## Update Coupling

- If image masters or prompt records change, rebuild the asset library, site-asset inventory, and image pools, then run `scripts/check_assets.py`.
- If categories change, edit `scripts/asset_categories.py` (and the role/asset maps in the builders), update `docs/ASSET_SCHEMA.md`, then rebuild and check. Do not hand-add a `category` to a JSON file.
- If a page's image slot changes (added, removed, re-pointed, or made random), mirror it in `assets/photo-slots.json` and `docs/PHOTO_SLOTS.md`, then run `scripts/check_assets.py`; a fixed slot's image category must equal the slot's category, and a random slot's `pool` must be a non-empty category in `image-pools.json`.
- If served renditions, generated dimensions, or catalog measurements appear to need edits, change the master or generator instead. Masters live in `assets/masters/<category>/`; served web files in `assets/images/<category>/`.
- If routes, filenames, asset ownership, validation commands, or working-directory responsibilities change, update `AGENTS.md`, this `ONTOLOGY.md`, and the relevant `MEMORY.md`.
- If tooling or skills fail, add a concise tooling note to `MEMORY.md` and update the affected script, guide, or runbook when the fix is clear.

## Validation

Use the narrowest relevant checks:

```powershell
node --check site.js
node --check asset-library.js
python -m py_compile scripts/build_asset_library.py
python scripts/build_asset_library.py
python scripts/build_site_asset_inventory.py
python scripts/build_image_pools.py
python scripts/check_assets.py
git diff --check
```

## Memory Rule

Every task that changes files must append a short entry to project `MEMORY.md`. If the changed surface has a local `MEMORY.md`, append there too.
