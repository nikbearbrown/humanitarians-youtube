"""tools.py — what a tool actually is: a contract, not a function.

Episode 3 of "Agentic AI: From the Loop to MCP" (Humanitarians AI Fellows).

Episodes 1 and 2 built a loop that calls tools. This file looks at what a "tool"
actually IS from the model's side of the wire — and the answer is uncomfortable:
the model never receives your function. It receives a name, a description, and a
parameter schema. Your implementation stays on your machine.

Runs with no dependencies and no API key:

    python3 tools.py
"""

from __future__ import annotations

import inspect
import json
import textwrap
from typing import Callable

# --- the tools, carried forward from episodes 1 and 2 ---------------------
# Same functions. The only thing this episode changes is what we write ABOVE them.


def read_file(path: str) -> str:
    """Read a UTF-8 text file from the project directory and return its contents.

    Use this when you need the actual text of a file. Do NOT use it to test whether
    a file exists, and do not call it twice with the same path — a missing file
    raises FileNotFoundError, and that error is the observation.
    """
    return "region,units\nnortheast,12\nmidwest,9\nsouth,14"


def count_rows(text: str) -> str:
    """Count the data rows in a CSV string, excluding the header line.

    Use this on text you have already read. Do NOT use it to count columns, and do
    not pass it a file path — it operates on contents, not on names.
    """
    return str(len(text.strip().splitlines()) - 1)


# --- the schema builder ---------------------------------------------------
# This is the beat B05 shows on screen, verbatim.

JSON_TYPES = {str: "string", int: "integer", float: "number", bool: "boolean"}


def to_schema(fn: Callable) -> dict:
    """Build the tool definition the model actually receives."""
    params = inspect.signature(fn).parameters.values()
    return {
        "name": fn.__name__,
        "description": inspect.getdoc(fn),
        "input_schema": {
            "type": "object",
            "properties": {p.name: {"type": JSON_TYPES.get(p.annotation, "string")}
                           for p in params},
            "required": [p.name for p in params
                         if p.default is inspect.Parameter.empty],
        },
    }


# --- the three questions a description has to answer ----------------------

def wire_view(fn: Callable, width: int = 52) -> str:
    """The same payload as to_schema(), laid out to be read rather than parsed.

    Every character shown is taken from the schema; the description is wrapped and
    elided with its full length stated, so nothing is quietly hidden.
    """
    s = to_schema(fn)
    doc = " ".join(s["description"].split())
    head = textwrap.wrap(doc, width)[:3]
    props = ", ".join(f"{k}: {v['type']}" for k, v in s["input_schema"]["properties"].items())
    lines = [f'name           {s["name"]}',
             f'description    "{head[0]}']
    lines += [f'                {ln}' for ln in head[1:]]
    lines[-1] += f'..."  ({len(s["description"])} chars total)'
    lines += [f'input_schema   {{ {props} }}',
              f'required       {s["input_schema"]["required"]}',
              '',
              'not sent       the function body']
    return "\n".join(lines)


def audit(description: str) -> dict:
    """Keyword heuristic — NOT a linter. It checks for the surface markers of the
    three questions, which is enough to show that a four-word docstring answers
    exactly one of them."""
    d = (description or "").lower()
    return {
        "what it returns": any(w in d for w in ("return", "contents", "count")),
        "when to use it":  "use this" in d or "use it" in d,
        "when not to":     "do not" in d or "not use" in d,
    }


def vague_read_file(path: str) -> str:
    """Reads a file."""
    return "region,units\nnortheast,12\nmidwest,9\nsouth,14"


def _report(fn: Callable) -> str:
    doc = inspect.getdoc(fn) or ""
    marks = "  ".join(f"{'YES' if v else 'no ':<3} {k}" for k, v in audit(doc).items())
    return f"{len(doc):>3} chars   {marks}"


if __name__ == "__main__":
    print("WHAT THE MODEL RECEIVES FOR read_file")
    print(json.dumps(to_schema(read_file), indent=2))

    print("\nTHE SAME PAYLOAD, LAID OUT TO BE READ")
    print(wire_view(read_file))

    print("\nSAME FUNCTION, TWO CONTRACTS")
    print(f"  vague    {_report(vague_read_file)}")
    print(f"  specific {_report(read_file)}")
    body = lambda fn: inspect.getsource(fn).split('"""')[-1].strip()
    print(f"\n  function bodies identical: {body(read_file) == body(vague_read_file)}")
