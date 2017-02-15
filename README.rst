To CBZ
======

**ToCBZ** adds helper scripts to make it easier to convert image folders
into "cbz" and "cb7" files. "cbz" and "cb7" are file formats compatible
with the most popular "comic readers" around, like mcomix_ and okular_.

Install
=======

.. code-block::shell
    pip install --user -e git+https://github.com/italomaia/to-cbz.git

Usage
=====

>>> to_cbz.py image-folder # image-folder.cbz
>>> to_cb7.py image-folder # image-folder.cb7
>>> to_7z.py image-folder # image-folder.7z
>>> to_cb7.py * # all folders are converted to cb7

Note
====

cbz and cb7 are equally compatible with comic readers. The big
difference between then is the trade-off. cbz files are larger,
but faster to load, while cb7 are smaller, but much slower.

Convert your folders to the format that is most convenient to
you.

.. _mcomix: https://sourceforge.net/p/mcomix/wiki/Home/
.. _okular: https://okular.kde.org/
