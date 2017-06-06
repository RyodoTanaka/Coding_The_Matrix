#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dict2list(dct, keylist) : return [dct[i] for i in keylist]

dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b', 'c', 'a']

print dict2list(dct, keylist)
