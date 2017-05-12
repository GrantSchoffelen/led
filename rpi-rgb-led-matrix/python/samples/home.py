#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        pos = canvas.width
        print(pos)
        font = graphics.Font()
        font.LoadFont("../../fonts/7x13.bdf")

        red = graphics.Color(255, 0, 0)
        graphics.DrawLine(canvas, 5, 5, 22, 13, red)

        blue = graphics.Color(0, 0, 255)
        len = graphics.DrawText(canvas, font, 2, 16, blue, "Whats up")

        pos -= 1
        if (pos + len < 0):
            pos = canvas.width

        time.sleep(0.05)
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)



# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
