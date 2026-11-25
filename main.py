"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The roast: a frayed charger cable that only works at one exact angle.
Everyone with a dying cable knows the ritual — bend it just so, prop
the phone against a book, and then freeze, because breathing wrong
kills the connection. The joke lands on that shared recognition:
charging has stopped being a chore and become a yoga pose, and the
pose has a name, because the cable is the one giving the orders now.
"""

import os

LINE = (
    "My charger cable only works at one exact angle, so charging "
    "my phone is a two-hour yoga pose called 'please don't move'."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the line comfortably inside.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
