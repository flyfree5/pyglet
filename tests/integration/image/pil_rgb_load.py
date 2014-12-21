"""Test RGB load using PIL.  You should see the rgb.png image on
a checkboard background.
"""

__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

import unittest
from . import base_load

from pyglet.image.codecs.pil import *


class TEST_PIL_RGB_LOAD(base_load.TestLoad):
    texture_file = 'rgb.png'
    decoder = PILImageDecoder()