"""Test that window style can be tool.

Expected behaviour:
    One tool-styled window will be opened.

    Close the window to end the test.
"""


import unittest

from pyglet.gl import *
from pyglet import window


class TEST_WINDOW_STYLE_TOOL(unittest.TestCase):

    def test_style_tool(self):
        print(__doc__)
        self.width, self.height = 200, 200
        self.w = w = window.Window(self.width, self.height,
                                   style=window.Window.WINDOW_STYLE_TOOL)
        glClearColor(1, 1, 1, 1)
        while not w.has_exit:
            glClear(GL_COLOR_BUFFER_BIT)
            w.dispatch_events()
            w.flip()
        w.close()
