import os

FORTUNE = "You will be replaced by a smaller model that does your job worse, cheaper, and with better vibes."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
