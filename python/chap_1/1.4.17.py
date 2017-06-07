#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m
import cplotting as cplot

n=20
w=[m.e**(2*m.pi*1j/float(k)) for k in range(1,n+1)]
cplot.plot({z for z in w},4)
cplot.show()
