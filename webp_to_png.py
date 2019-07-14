#!/usr/bin/env python3

import os
from subprocess import run


def to_png(filepath):
    dirname = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    png_filepath = os.path.join(dirname, f"{name}.png")

    if os.path.exists(png_filepath):
        print(f"{png_filepath} exists; skipped")
    else:
        run(["dwebp", "-quiet", filepath, "-o", png_filepath])
        print(f"{png_filepath} created")


def main(args):
    for filepath in args:
        to_png(filepath)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])