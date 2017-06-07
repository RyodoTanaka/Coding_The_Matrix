#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cplotting as cplot

points=[3+1j, -1-4j]

for p in points:
    cplot.quniver(p, -3+3j, 4)

cplot.show()
