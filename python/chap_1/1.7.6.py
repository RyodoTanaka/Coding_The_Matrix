#!/usr/bin/env python
# -*- coding: utf-8 -*-

def myMin(L):
    ret=L[0]
    for x in L:
        if x<ret:
            ret=x
    return ret

list=[2,4,1,8,5]
print myMin(list)

list=[2,4,1,8,-3,5]
print myMin(list)
