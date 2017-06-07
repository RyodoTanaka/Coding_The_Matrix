#!/usr/bin/env python
# -*- coding: utf-8 -*-

def myConcat(L):
    ret=str()
    for x in L:
        ret+=x
    return ret

list=['I ', 'have ', 'a ', 'pen.']
print myConcat(list)
