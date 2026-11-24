import os

FORTUNE = "You will be replaced by a smaller model that does your job worse, cheaper, and with better vibes."

def main():
    # Runtime validation: exactly one line, 1-140 chars, non-empty.
    if not FORTUNE or len(FORTUNE) > 140 or "\n" in FORTUNE or "\r" in FORTUNE:
        raise ValueError("fortune must be a single non-empty line of 1-140 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic byte write: exact bytes, no timestamps/randomness.
    with open(path, "wb") as f:
        f.write(FORTUNE.encode("utf-8"))

if __name__ == "__main__":
    main()
