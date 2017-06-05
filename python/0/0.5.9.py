#!/usr/bin/env python
# -*- coding: utf-8 -*-

S={1,2,3,4}
T={3,4,5,6}

ret = {x for x in S for y in T if x==y}
print ret
