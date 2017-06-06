#!/usr/bin/env python
# -*- coding: utf-8 -*-

def list2dict(L, keylist) : return {keylist[i]:L[i] for i in range(len(keylist))}

L=['A', 'B', 'C']
keylist=['a', 'b', 'c']

print list2dict(L, keylist)
