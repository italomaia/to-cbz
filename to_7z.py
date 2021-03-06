#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import subprocess
from multiprocessing import Pool


def cmd_exists(cmd):
    return subprocess.call(
        "type " + cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ) == 0


def make_filename(dirname, ext):
    if dirname.endswith("/"):
        dirname = dirname[:-1]
    return "%s.%s" % (dirname, ext)


def to_7z(dirname):
    cb7_filename = make_filename(dirname, '7z')
    subprocess.call(['7za', 'a', '-t7z', cb7_filename, dirname])


def main(args):
    if not cmd_exists("7za"):
        print("7za could not be found. Exit.")
        exit(0)

    pool = Pool()
    for arg in args:
        if os.path.isdir(arg):
            pool.apply_async(to_7z, [arg], callback=lambda r:None)
        else:
            print(arg, "is a file. Ignoring.")

    if not args:
        print("Nothing to do.")

    pool.close()
    pool.join()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
