# Repository Guidelines

## Project Structure & Module Organization

Fast64 is a Python add-on for Blender that imports and exports Nintendo 64 assets. The root `__init__.py` contains add-on metadata and registration. Shared implementation lives in `fast64_internal/`; `f3d/` handles materials and display lists, while `sm64/`, `z64/`, and `mk64/` contain game-specific features. Reference data lives in `fast64_internal/data/`, including XML definitions. Blender resources such as `f3d_material_library.blend` sit alongside their modules. `scripts/oot/` contains skeleton utilities, and `images/` holds documentation images. Updater code is in the root and `fast64_updater/`.

## Build, Test, and Development Commands

- `python -m pip install "black>=23,<24"` installs the required formatter version.
- `python -m black --check .` checks formatting, matching the GitHub Actions check on pushes and pull requests.
- `python -m black path/to/changed_file.py` formats a changed file; `python -m black .` formats the repository.

There is no standalone build command. Install the repository ZIP through Blender's **Edit > Preferences > Add-ons > Install**, enable Fast64, and access its tools in the 3D View sidebar. The README requires Blender 3.2+ and recommends 4.0+. Runtime code depends on Blender's `bpy` and `mathutils` modules.

## Coding Style & Naming Conventions

Use four-space indentation and Black 23 with the 120-character line limit and Python 3.10 target configured in `pyproject.toml`. Match neighboring naming conventions: the code mixes snake_case helpers, camelCase legacy APIs, and game-prefixed Blender classes such as `OOT_SaveRestPose`. Keep game-specific changes within their game module. Black excludes the externally sourced `addon_updater.py` and `addon_updater_ops.py`; avoid incidental edits to those files.

## Testing Guidelines

No automated test suite or coverage threshold is configured. Validate behavior in Blender using a small representative scene: exercise the changed operator, inspect exported assets or re-import them, and check for errors. For UI or material changes, inspect the affected panels and viewport. Record the Blender version, reproduction steps, and results in the pull request. Run the formatting check before submitting.

## Commit & Pull Request Guidelines

History uses short, informal subjects without a consistent enforced prefix. Write descriptive, action-oriented subjects identifying the affected feature. Keep commits focused. Pull requests should explain the behavior change, link relevant issues, and describe validation; include screenshots for visible UI or rendering changes.