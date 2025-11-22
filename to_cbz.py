#!/usr/bin/env python3

import os
import zipfile
from multiprocessing import Pool


def make_filename(dirname: str, ext: str):
    if dirname.endswith("/"):
        dirname = dirname[:-1]
    return "%s.%s" % (dirname, ext)


def to_cbz(dirname: str):
    cbz_filename = make_filename(dirname, "cbz")
    zfile = zipfile.ZipFile(cbz_filename, "w")

    for rootpath, _, filenames in os.walk(dirname):
        for filename in filenames:
            abs_filename = os.path.join(rootpath, filename)
            zfile.write(abs_filename)
    zfile.close()


def main(args: list[str]):
    pool = Pool()

    for arg in args:
        if os.path.isdir(arg):
            _ = pool.apply_async(to_cbz, [arg], callback=lambda r: None)
        else:
            print(arg, "is a file. Ignoring.")

    if not args:
        print("Nothing to do.")

    pool.close()
    pool.join()


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
