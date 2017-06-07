#!/usr/bin/env python
# -*- coding: utf-8 -*-

def myProduct(L):
    ret=1
    for x in L:
        ret*=x
        
    return ret

list=[1,2,4,8,5]
print myProduct(list)
