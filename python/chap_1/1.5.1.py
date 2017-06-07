#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GF2 import one
from GF2 import zero

def str2GF2(string):
    return one if string=='1' else zero
def GF22str(gf2):
    return '1' if gf2==one else '0'

def f(data, key, dictionary):
    ret=str()
    for word in data:
        tmp=str()
        for i, char in enumerate(word):
            tmp+=GF22str( str2GF2(char)+str2GF2(key[i]) )
        ret+=dictionary[tmp]

    return ret

# get data
raw_data="10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010"
data=raw_data.split()

# make dictionary
d={str(format(k,'05b')):chr(ord('A')+k) for k in range(26)}
d['11010']=' '
for k in range(0b11011,0b11111+1):
    d[str(format(k,'05b'))]='.'

# make all patterns of key
key=[str(format(x,'05b')) for x in range(0b11111)]

# see message
for k in key:
    message=f(data, k, d)
    if '.' not in message:
        print "key :", k, message

# ==================================
#    The message is : EVA IS EVIL
# ==================================
