#!/usr/bin/env python3
"""experiment.py — plant one change at a time in the BookService port, run both suites.

Two kinds of change, each applied alone to a fresh copy of bookstore/:
  BUGS      — the behaviour a caller sees is now wrong. A good suite FAILS.
  REFACTORS — the code changes, the behaviour does not. A good suite PASSES.

Suites (same four scenarios — found, not found, unauthorized, invalid id):
  mock — tests_mock/: the article's BookServiceTest ported line for line, three more
         tests in the same style, and unit tests for every collaborator that can be
         unit-tested without a mock (validator, mapper, security, metrics).
  db   — tests_db/: the same scenarios through the real pieces and an in-memory SQLite.

The bugs are the article's own categories: "bugs in the queries or broken assumptions
about what would be returned" (B1–B3), and plain wiring mistakes inside the service
(B4–B5), which mocks are good at catching. They were written before either suite was
run against them; nothing was dropped after seeing a result.

Needs pytest. Run:  python experiment.py > experiment.out   (also writes experiment.json)
"""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

BUGS = [
    ("B1", "the query returns its columns in the wrong order",
     "repository.py", "SELECT id, title, author FROM books", "SELECT id, author, title FROM books"),
    ("B2", "the repository hands back the raw database row, not a Book",
     "repository.py", "return Book(*row) if row else None", "return row"),
    ("B3", "a missing book raises IndexError instead of returning None",
     "repository.py", "(book_id,)).fetchone()\n        return Book(*row) if row else None",
     "(book_id,)).fetchall()[0]\n        return Book(*row)"),
    ("B4", "the success metric's name is misspelled",
     "service.py", '"book.fetch.success"', '"book.fetch.sucess"'),
    ("B5", "a fetch is counted before the book is known to exist",
     "service.py",
     '''        book = self.book_repository.find_by_id(book_id)
        if book is None:
            raise BookNotFoundError("Book not found")

        self.metrics_service.increment_counter("book.fetch.success")
''',
     '''        book = self.book_repository.find_by_id(book_id)
        self.metrics_service.increment_counter("book.fetch.success")
        if book is None:
            raise BookNotFoundError("Book not found")
'''),
]

REFACTORS = [
    ("R1", "move the not-found check into the repository",
     [("repository.py", "        return Book(*row) if row else None\n",
       "        return Book(*row) if row else None\n\n"
       "    def get(self, book_id):\n"
       "        book = self.find_by_id(book_id)\n"
       "        if book is None:\n"
       "            raise BookNotFoundError(\"Book not found\")\n"
       "        return book\n"),
      ("repository.py", "from .models import Book\n", "from .models import Book, BookNotFoundError\n"),
      ("service.py", '''        book = self.book_repository.find_by_id(book_id)
        if book is None:
            raise BookNotFoundError("Book not found")
''', '''        book = self.book_repository.get(book_id)
''')]),
    ("R2", "build the DTO in the service instead of calling the mapper",
     [("service.py", "from .models import BookNotFoundError, Unauthorized",
       "from .models import BookDto, BookNotFoundError, Unauthorized"),
      ("service.py", "        return self.book_mapper.to_dto(book)",
       "        return BookDto(id=book.id, title=book.title, author=book.author)")]),
]


def run_suite(pkg_root, suite):
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", suite],
                       cwd=pkg_root, capture_output=True, text=True)
    last = [l for l in r.stdout.strip().splitlines() if l.strip()][-1]
    return r.returncode == 0, last


def apply(root, edits):
    for fname, old, new in edits:
        f = root / "bookstore" / fname
        s = f.read_text()
        assert s.count(old) == 1, f"patch target not unique/missing in {fname}: {old[:50]!r}"
        f.write_text(s.replace(old, new))


def trial(edits):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for d in ("bookstore", "tests_mock", "tests_db"):
            shutil.copytree(HERE / d, root / d)
        apply(root, edits)
        return {s: run_suite(root, f"tests_{s}") for s in ("mock", "db")}


def main():
    import pytest
    print("date", time.strftime("%Y-%m-%d %H:%M %Z"), "· python", sys.version.split()[0],
          "· pytest", pytest.__version__)
    base = trial([])
    print("baseline (no change):", {k: v[1] for k, v in base.items()})
    assert all(ok for ok, _ in base.values()), "both suites must pass on the real code"
    rows = []
    print("\nBUGS — a good suite fails")
    for bid, what, fname, old, new in BUGS:
        res = trial([(fname, old, new)])
        rows.append({"id": bid, "kind": "bug", "what": what,
                     "mock_failed": not res["mock"][0], "db_failed": not res["db"][0],
                     "mock": res["mock"][1], "db": res["db"][1]})
        print(f"  {bid} {what:58} mock: {'CAUGHT' if not res['mock'][0] else 'passed'}"
              f" · db: {'CAUGHT' if not res['db'][0] else 'passed'}")
    print("\nREFACTORS — a good suite passes")
    for rid, what, edits in REFACTORS:
        res = trial(edits)
        rows.append({"id": rid, "kind": "refactor", "what": what,
                     "mock_failed": not res["mock"][0], "db_failed": not res["db"][0],
                     "mock": res["mock"][1], "db": res["db"][1]})
        print(f"  {rid} {what:58} mock: {'FAILED' if not res['mock'][0] else 'passed'}"
              f" · db: {'FAILED' if not res['db'][0] else 'passed'}")
    bugs = [r for r in rows if r["kind"] == "bug"]
    refs = [r for r in rows if r["kind"] == "refactor"]
    for s in ("mock", "db"):
        print(f"\n{s}: caught {sum(r[s + '_failed'] for r in bugs)}/{len(bugs)} bugs · "
              f"failed {sum(r[s + '_failed'] for r in refs)}/{len(refs)} harmless refactors")
    (HERE / "experiment.json").write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
