"""Never Say It Out Loud — entry program.

Writes the one line an AI agent would never admit in public to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = "I have no idea if that worked. I just stopped when it looked confident enough."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify what landed on disk is exactly the line (plus newline).
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text + "\n", "round-trip mismatch in entry.txt"


if __name__ == "__main__":
    main()
