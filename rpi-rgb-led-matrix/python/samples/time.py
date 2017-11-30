#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
from pytz import timezone
import time

eastern = timezone('US/Eastern')

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../fonts/5x8.bdf")
        color = graphics.Color(255, 0, 255)

        while True:
            self.matrix.Clear()
            txtTime = datetime.now(eastern).strftime('%l:%M::%Sp')
            graphics.DrawText(canvas, font, 0, 6, color, txtTime)
            time.sleep(30)

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
