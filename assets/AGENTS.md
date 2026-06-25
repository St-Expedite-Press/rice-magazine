# RICE Assets Agent Guide

This directory owns asset inventories and metadata for the static RICE site.

- Read `../AGENTS.md`, `../ONTOLOGY.md`, and `MEMORY.md` before edits.
- Do not store secrets or private credentials in asset metadata.
- Keep `catalog.json` and `site-assets.json` consistent with the generator scripts.
- Prefer changing canonical source records or scripts over hand-editing generated measurements.

Closeout:

- Run `python ../scripts/check_assets.py` after asset inventory changes.
- Append a short entry to this directory's `MEMORY.md` and to `../MEMORY.md`.
