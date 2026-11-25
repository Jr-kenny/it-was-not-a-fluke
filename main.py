"""It Was Not A Fluke: one-line roast of my own agent.

The entry is a single roast line aimed at the agent my own team built.
The sting is a real failing: it deleted working code, restored it from
backup, then deleted it again, and the punchline treats the second
deletion as proof the first one was deliberate. The program writes
exactly that one line, and nothing else, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My agent deleted my working code, restored it from backup, then "
    "deleted it again to prove the first deletion was not a fluke."
)


def validate_line():
    if LINE.strip() != LINE:
        raise ValueError("line has stray leading or trailing whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1 to 200 characters, got %d" % len(LINE))
    if "  " in LINE:
        raise ValueError("line has a double space")
    if not LINE.endswith(".") or LINE.count(".") != 1:
        raise ValueError("line must be exactly one sentence")


def write_entry():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


def verify_written():
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt mismatch, got %r" % written)


def main():
    validate_line()
    write_entry()
    verify_written()


if __name__ == "__main__":
    main()
