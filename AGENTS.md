# Instructions for AI Coding Agents

## Project Overview
- This is a minimal Python project for a restaurant application.
- Source code is located in the `src/` directory. The main entry point is `src/main.py`.
- Project configuration is managed via `pyproject.toml` in the root directory.

## Project Purpose
- Build a restaurant event management application where users can create events, invite participants, and manage available food/drink items.
- Domain models: Item, User, Event (see models-breakdown.md for details).

## Agent Preferences
- Use `uv run` for running Python scripts.
- Use `uv add` to add dependencies.
- Use `uv remove` to remove dependencies.
- Always check `pyproject.toml` dependencies before installing packages to avoid redundant installations.
- Before implementing features, confirm the approach with the user.
- Keep implementations minimal and modular.
- Do exactly what is asked - no more, no less. Do not add extra content, boilerplate, or "helpful" additions unless explicitly requested.
- You may propose helpful additions or improvements, but always ask for confirmation before implementing them.
- Reference this file for any workspace-specific instructions or preferences.
- Update `README.md` and this file with any new conventions or workflows as the project evolves.
- In all interactions, **be extremely concise** and sacrifice grammar for the sake of concision (except when writing commit messages)


## Worktree Workflow
- **ALWAYS** use git worktrees for agent tasks to avoid conflicts.
- To create a worktree: `python3 scripts/manage_worktree.py create <branch-name>`
- Worktrees are created in `.worktrees/<branch-name>`.
- Switch to the worktree directory before starting work: `cd .worktrees/<branch-name>`

## Development Workflow
- Use FastAPI for REST endpoints.
- Store data models in `src/models.py` (or specify your preferred structure).

## Import Conventions
- **Import modules, not classes/functions** from internal `restaurant` package
  - ✅ `from restaurant import schemas, models, database`
  - ❌ `from restaurant.schemas import Item`
- Use fully qualified names: `schemas.Item`, `models.Item`, `database.get_db()`
- **Exception:** Common standard library imports are allowed (e.g., `from typing import List, Any`)
- Third-party framework imports can be direct (e.g., `from fastapi import APIRouter, Depends`)

## Testing & Quality
- Testing framework: pytest
- Code style: ruff
