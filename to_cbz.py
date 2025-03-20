#!/usr/bin/env python3

import os
import zipfile
from multiprocessing import Pool


def make_filename(dirname, ext):
    if dirname.endswith("/"):
        dirname = dirname[:-1]
    return "%s.%s" % (dirname, ext)


def to_cbz(dirname):
    cbz_filename = make_filename(dirname, 'cbz')
    zfile = zipfile.ZipFile(cbz_filename, "w")

    for rootpath, dirnames, filenames in os.walk(dirname):
        for filename in filenames:
            abs_filename = os.path.join(rootpath, filename)
            zfile.write(abs_filename)
    zfile.close()


def main(args):
    pool = Pool()
    for arg in args:
        if os.path.isdir(arg):
            pool.apply_async(to_cbz, [arg], callback=lambda r:None)
        else:
            print(arg, "is a file. Ignoring.")

    if not args:
        print("Nothing to do.")

    pool.close()
    pool.join()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
