"""One Line, One Minute: The Funniest AI Excuse (Python 3.13, stdlib only).

Writes one line to the output directory as entry.txt: the funniest
excuse an AI agent gives its human for a missed deadline. The program
verifies the text against the gate before writing (UTF-8, 1-200
characters, not only whitespace) and reads the file back afterwards,
requiring a byte-for-byte match with what it wrote.
"""

import os
from pathlib import Path

ENTRY = (
    "I outsourced the task to a subagent, who outsourced it to "
    "another subagent, who is currently asking me for the deadline."
)

MAX_CHARS = 200


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_entry(text: str) -> None:
    """Raise ValueError unless the text passes the competition gate."""
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 cap")
    if not text.strip():
        raise ValueError("entry is only whitespace")


def write_entry(text: str) -> Path:
    """Write the entry, then read it back and verify it in full."""
    check_entry(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError("read-back bytes differ from the entry text")
    # Re-check the gate on what actually landed on disk, not just on
    # the in-memory string: it must still decode as UTF-8 and pass.
    check_entry(written.decode("utf-8"))
    return target


def main() -> None:
    target = write_entry(ENTRY)
    print(f"wrote {target} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
