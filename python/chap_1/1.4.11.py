#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image import file2image
import cplotting as cplot

def f(S):
    r = [z.real for z in S]
    c = [z.imag for z in S]

    r_center = (min(r)+max(r))/2.
    c_center = (min(c)+max(c))/2.

    return [z.real-r_center + (z.imag-c_center)*1j for z in S]

data=file2image('img01.png')
pts = [x + (len(data)-y)*1j for y in range(len(data)) for x in range(len(data[y])) if data[y][x][0] < 120]
cpts=f(pts)
cplot.plot(cpts,190)
cplot.show()
