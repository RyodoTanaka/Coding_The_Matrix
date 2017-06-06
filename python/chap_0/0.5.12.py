#!/usr/bin/env python
# -*- coding: utf-8 -*-

la=[ [0.25,0.75,0.1], [-1,0], [4,4,4,4] ]
lb=[ [1,0,1,0,1], [1,2,3,4], [0.1,0.2,0.3] ] # lb also works (answer is 13.6)

ret = sum([sum(x) for x in la])
print ret
