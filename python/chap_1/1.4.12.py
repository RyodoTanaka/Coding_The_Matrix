#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image import file2image
import cplotting as cplot

data=file2image('img01.png')
pts = [x + (len(data)-y)*1j for y in range(len(data)) for x in range(len(data[y])) if data[y][x][0] < 120]

cplot.plot({z*1j*0.5 for z in pts},190)
cplot.show()
