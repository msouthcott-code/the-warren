# The Warren 🐇

A tiny (and intentionally imperfect) carrot inventory manager, built as a
practice repo for trying out **CodeRabbit** code review.

## Files

- `warren.py` — main entry point, ties everything together
- `carrot_stash.py` — carrot inventory logic
- `burrow_utils.py` — small helper functions
- `lettuce_ledger.py` — SQLite-backed record keeping

## Running it

```bash
pip install -r requirements.txt
python warren.py
```

## Why is this code kind of bad?

On purpose! This repo has a handful of planted issues — things like a
hardcoded API key, a SQL injection risk, a mutable default argument, a
bare `except`, an unused import, and a couple of logic bugs — so that
CodeRabbit has real things to catch when it reviews a pull request.

Try opening a PR against `main` with a small change and watch what
CodeRabbit flags.
