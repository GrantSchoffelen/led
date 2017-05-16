#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
	super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../fonts/5x7.bdf")
        color = graphics.Color(0, 255, 255)
	
	while True:
	    self.matrix.Clear()
	    txtTime2 = time.strftime('%l:%M:%S%p')
	    graphics.DrawText(canvas, font, -5, 6, color, txtTime2)
	    time.sleep(1)

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
