# RICE Scripts Agent Guide

This directory owns Python build and validation scripts for the static asset system.

- Read `../AGENTS.md`, `../ONTOLOGY.md`, and `MEMORY.md` before edits.
- Keep scripts dependency-light and compatible with local PowerShell invocation.
- Avoid changing generated outputs directly; update scripts and rerun generators.
- Preserve deterministic catalog and derivative behavior.

Closeout:

- Run `python -m py_compile build_asset_library.py` for script edits.
- Run relevant asset build/check scripts when generator behavior changes.
- Append a short entry to this directory's `MEMORY.md` and to `../MEMORY.md`.
