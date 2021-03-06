#!/usr/bin/env python
# -*- coding: utf-8 -*-
from samplebase import SampleBase
from rgbmatrix import graphics
import requests
import json
import math
import time
from datetime import datetime
from pytz import timezone
import time

eastern = timezone('US/Eastern')

icons = {
    'clear-day' : 'clear-day',
    'clear-night': 'clear-night',
    'rain':'rain',
    'snow':'snow',
    'sleet': 'sleet',
    'wind': 'wind',
    'fog' : 'fog',
    'cloudy': 'cloudy',
    'partly-cloudy-day': 'partly-cloudy-day',
    'partly-cloudy-night': 'partly-cloudy-night'
}

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        r = requests.get('https://api.darksky.net/forecast/80898f5e97e9c9ee461ecf0f94643a4f/40.783428,-73.966248')
        res = json.loads(r.text)
        current_weather = icons[res['currently']['icon']]
        future_8 = icons[res['hourly']['data'][7]['icon']]
        future_16 = icons[res['hourly']['data'][15]['icon']]
        current_temp = math.ceil(res['currently']['apparentTemperature'])
        # textTemp = ('%d°F, %s' % (current_temp, current_weather) )
        textTemp = ('%d°F' % current_temp)
        textTemp = textTemp.decode("utf8")
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../fonts/4x6.bdf")
        color = graphics.Color(255, 0, 255)

        while True:
            self.matrix.Clear()
            txtTime = datetime.now(eastern).strftime('%l:%Mp')
            graphics.DrawText(canvas, font, 3, 7, color, txtTime)
            graphics.DrawText(canvas, font, 45, 7, color, textTemp)
            time.sleep(60)

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
