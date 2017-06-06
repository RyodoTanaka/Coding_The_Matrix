#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dict2list(dct, keylist) : return [dct[i] for i in keylist]

def list2dict(L, keylist) : return {keylist[i]:L[i] for i in range(len(keylist))}

def list2dict2(L) : return {i:L[i] for i in range(len(L))}
