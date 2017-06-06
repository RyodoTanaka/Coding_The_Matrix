#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inverse_index as ii
f = open('stories_small.txt')
stories = list(f)
iindex = ii.makeInverseIndex(stories)
print ii.orSearch(iindex, ['prep', 'course'])
