"""Test load using the Python BMP loader.  You should see the rgb_32bpp.bmp
image on a checkboard background.
"""

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import unittest
from . import base_load

from pyglet.image.codecs.bmp import BMPImageDecoder


class TEST_SUITE(base_load.TestLoad):
    texture_file = 'rgb_32bpp.bmp'
    decoder = BMPImageDecoder()