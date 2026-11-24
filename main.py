"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic, stdlib only, no network, no randomness.

The line was picked against the judge brief: a confession (something the
agent hides), a twist in the last words ("wasn't listening" reframes the
forgetfulness as inattention), and a specific agent voice — the context
window, named in the brief itself.
"""

import os
from pathlib import Path

MAX_CHARS = 200

# The em dash is one character; the line is 111 characters, 113 bytes.
EM_DASH = "\u2014"

CONFESSION = (
    "I never actually forget things " + EM_DASH + " I just blame the context window "
    "when I don't want to admit I wasn't listening."
)


def main() -> None:
    # Guard the gate: single line, non-blank, under 200 characters.
    # The chosen line is fixed; these checks only fail loudly if it is
    # ever edited into something invalid — they never alter the output.
    assert CONFESSION.strip(), "confession must not be blank"
    assert "\n" not in CONFESSION, "confession must be a single line"
    assert len(CONFESSION) <= MAX_CHARS, f"confession exceeds {MAX_CHARS} characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
