#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inverse_index import makeInverseIndex

print "==== Small Stories ===="
f = open('stories_small.txt')
stories = list(f)
wdict = makeInverseIndex(stories)
print wdict['prep']
print wdict['all']

print "==== Big Stories ===="
f = open('stories_big.txt')
stories = list(f)
wdict = makeInverseIndex(stories)
print wdict['prep']
print wdict['all']
