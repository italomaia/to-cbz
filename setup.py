"""to_cbz manager."""

from distutils.core import setup

setup(
    name='to_cbz',
    version='0.2.6',
    description='Convert foldes into cbz files.',
    author='Italo Maia',
    url='https://github.com/italomaia/to-cbz',
    scripts=[
        'to_cbz.py',
        'to_cb7.py',
        'to_7z.py',
        'webp_to_png.py',
    ]
)
