"""
# Entry validated: output is 1-30 chars, one word, deterministic.
Entrypoint that writes the word 'Gaspol' to the designated output file.
"""

import os


WORD = "Gaspol"


def main():
    if not (1 <= len(WORD) <= 30 and WORD.strip() and ' ' not in WORD):
        raise ValueError("Invalid word format or length")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)

    print(output_path)
    print(len(WORD))


if __name__ == "__main__":
    main()
