#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tuple_sum(A, B):
    ret=[]
    for anum, a in enumerate(A):
        tmp=tuple()
        for bnum, b in enumerate(B[anum]):
            tmp+=(a[bnum] + b, )
        ret.append(tmp)
    return ret


A=[(1,2), (10,20)]
B=[(3,4), (30,40)]
C=[(5,6), (50,60)]

ret = tuple_sum(A, B)
print ret
ret = tuple_sum(ret, C)
print ret
