#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_filter(L):
    return [[y for y in range(1,x+1) if x>0] for x in L]

list=[0,1,2,4,8]

print my_filter(list)
