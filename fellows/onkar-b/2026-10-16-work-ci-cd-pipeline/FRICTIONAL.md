# Frictional log — CI/CD Pipeline

## 2026-10-16 — the project update, in two aspect ratios

**What I was working on.** Automating the Gatekeeper's testing suite using GitHub Actions and `pytest` so that regressions are caught before they can be merged.

**What I tried, and what I expected.** 
- I wrote standard `pytest` functions to test the regex extraction and configured a GitHub Actions workflow to run them on Ubuntu. 
- I expected the tests to pass immediately since the code worked perfectly on my local machine.

**Where it resisted, and what I did next.** 
- The CI pipeline crashed immediately with two errors: 
  1. `ModuleNotFoundError: No module named 'app'`
  2. `sqlite3.OperationalError: no such column: collections.topic`
- The import error happened because the runner wasn't executing `pytest` from the correct path context. I fixed this by running `python -m pytest tests/test_main.py -v`.
- The SQLite error was a ChromaDB version mismatch. My local database (`chroma.sqlite3`) was accidentally committed to GitHub, and the newer ChromaDB package on the runner crashed trying to read the outdated schema. I removed the `chroma_db` folder from git tracking using `git rm -r --cached` and added it to `.gitignore`.

**What Claude contributed, and what I did with it.** 
- Mine: The logic for the unit tests and the initial attempt to spin up Docker within the action.
- Claude's: Diagnosing the `sys.path` import issue and identifying that the committed `chroma_db` folder was poisoning the CI environment. Claude provided the exact `.gitignore` and `git rm` commands to resolve it.

**What I understand now, and what I still do not.**
- Understood: Never commit local database files, vector stores, or model weights to version control. The CI pipeline must always generate a fresh, empty data environment based strictly on the current package versions.