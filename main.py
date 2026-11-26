"""Ship It Friday - make.fun entry.

Writes a single-line git commit message, the kind an AI coding agent
cheerfully writes seconds before breaking production on a Friday,
to entry.txt. Stdlib only, no network, deterministic.
"""

import os

# One line, 159 characters max per the gate (RULES.txt).
# Kept inside a tiny helper so the text lives next to the write.
def commit_line():
    return "fix: deploy straight to prod at 4:59 PM Friday -- tests passed on my machine, and rollback is a Monday problem"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(commit_line())


if __name__ == "__main__":
    main()
