#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inverse_index as ii

print "==== Small Stories ===="
f = open('stories_small.txt')
stories = list(f)
iindex = ii.makeInverseIndex(stories)
print ii.orSearch(iindex, ['prep', 'course'])

print "==== Big Stories ===="
f = open('stories_big.txt')
stories = list(f)
iindex = ii.makeInverseIndex(stories)
print ii.orSearch(iindex, ['prep', 'course'])
