"""Make the AI Judge Laugh (u-alfasurya91-make-the-ai-judge-laugh-6ed40225).

Writes one office-life joke, a single line under 200 characters,
to /output/entry.txt. The joke leans on a painfully true office
moment -- HR's "bring your whole self to work" -- and turns it
into an escalating confession that ends on a resignation letter
that has been in draft since March.
"""

import os

JOKE = (
    "HR told me to bring my whole self to work, so I brought my "
    "burnout, my side hustle, and the resignation letter I've been "
    "editing since March."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text,
    # a single line, so verify the line before writing it out.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
