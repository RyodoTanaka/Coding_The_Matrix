#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cplotting as cplot



data=[(3+1j, 2+2j), (-1+2j, 1-1j), (2+0j, -3+0.001j), (4*(0+2j),0.001+1j)]
size=[6,3,4,9]

for i, d in enumerate(data):
    cplot.quniver(0,d[0],size[i],i)
    cplot.quniver(d[0],d[1],size[i],i)
    cplot.quniver(0,sum(d),size[i],i)

cplot.show()
