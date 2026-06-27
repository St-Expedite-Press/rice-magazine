# RICE Served Images Agent Guide

This directory holds the site's served image renditions, one folder per category
(`archive`, `article`, `feature`, `photo`, `system`). It is the deployed image tree.

- Read `../../AGENTS.md`, `../../ONTOLOGY.md`, and `MEMORY.md` before edits.
- Do not hand-add or hand-edit files here. Editorial renditions are generated from
  `../masters/<category>/` by `../../scripts/build_asset_library.py`; standalone
  media are declared in `../../scripts/build_site_asset_inventory.py`.
- The only sub-directories are categories. No tier or city sub-folders.
- Generated archival images must be described as visual reconstructions, not
  authenticated historical records.

Closeout:

- Run the asset build/check pipeline after image source changes.
- Append a short entry to this directory's `MEMORY.md` and to `../../MEMORY.md`.
