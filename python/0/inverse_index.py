#!/usr/bin/env python
# -*- coding: utf-8 -*-

def makeInverseIndex(strlist) :
    wdict={}
    for ln, line in enumerate(strlist):
        for word in set(line.split()):
            if word in wdict:
                wdict[word].append(ln)
            else:
                wdict[word]=[ln] 
    return wdict
