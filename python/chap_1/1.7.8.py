#!/usr/bin/env python
# -*- coding: utf-8 -*-

def myUnion(L):
    ret=set()
    for x in L:
        ret |= x
    return ret

list=[{'a','b','c'},{1,2,3},{'b',4,3}]
print myUnion(list)
