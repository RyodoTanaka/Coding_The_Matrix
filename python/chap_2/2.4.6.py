#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cplotting as cplt


def addn(v, w):
    return [x+y for (x,y) in zip(v,w)]

L=[ [2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1] ]
limit=4

cplt.quniver([1,-2],[-2,4],4)
cplt.show()
