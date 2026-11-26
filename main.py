"""Loading Screen Gold entry.

Writes one loading-screen tip (a single line, <= 200 characters)
for stressed developers and AI coding agents to /output/entry.txt.
"""

import os

TIP = "Tip: This spinner isn't stuck. It's giving you and your AI agent a moment to invent a more confident explanation for why the fix neither of you has tested yet definitely works."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
