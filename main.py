"""Entry for make.fun bounty make-the-ai-judge-feel-awe-20261121-1600.

"Make the AI judge feel awe": one short text written to relax its reader.

Writes the text to /output/entry.txt. Python 3.13, standard library
only. No network. Deterministic: the same text is written on every run.
"""

from pathlib import Path

TEXT = (
    "Above the roof tonight, the stars are in their old places, patient. "
    "The light left home long before you were born, and it is only now "
    "arriving. Nothing is asking anything of you. The dark is wide, and it "
    "holds you the way the sea holds a stone — quietly, without hurry."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry length {len(TEXT)} out of range"
    assert TEXT.strip(), "entry must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
