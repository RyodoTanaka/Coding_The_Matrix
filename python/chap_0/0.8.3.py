#!/usr/bin/env python
# -*- coding: utf-8 -*-

def row(p, n):
    return [x+p for x in range(n)]

ret=[row(x,20) for x in range(15)]
print ret

ret=[ [x+y for x in range(20)] for y in range(15) ]
print ret
