"""Test LA load using PIL.  You should see the la.png image on
a checkboard background.
"""

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import unittest
from . import base_load

from pyglet.image.codecs.pil import *


class TEST_PNG_LA(base_load.TestLoad):
    texture_file = 'la.png'
    decoder = PILImageDecoder()