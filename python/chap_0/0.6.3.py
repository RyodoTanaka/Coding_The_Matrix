#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dictutil

dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b', 'c', 'a']
print dictutil.dict2list(dct, keylist)

L=['A', 'B', 'C']
keylist=['a', 'b', 'c']
print dictutil.list2dict(L, keylist)
