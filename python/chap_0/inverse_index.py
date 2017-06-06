#!/usr/bin/env python
# -*- coding: utf-8 -*-

def makeInverseIndex(strlist):
    wdict={}
    for ln, line in enumerate(strlist):
        for word in set(line.split()):
            if word in wdict:
                wdict[word].append(ln)
            else:
                wdict[word]=[ln] 
    return wdict

def orSearch(inverseIndex, query):
    wset=set(list())
    for word in query:
        if word in inverseIndex:
            wset = wset | set(inverseIndex[word])
    return wset

def andSearch(inverseIndex, query):
    wset=set(list())
    for num, word in enumerate(query):
        if word in inverseIndex:
            if num==0:
                wset = wset | set(inverseIndex[word]) 
            else:
                wset = wset & set(inverseIndex[word]) 
    return wset
