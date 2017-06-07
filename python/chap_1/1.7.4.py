#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mySum(L):
    ret=0
    for x in L:
        ret+=x
        
    return ret

list=[1,2,4,8,5]

print mySum(list)
