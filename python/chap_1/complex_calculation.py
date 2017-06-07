#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m

def rotate(S, rotate):
    ret=[]
    theta=float()
    
    for z in S:
        if z.real>0:
            theta=m.atan(float(z.imag)/float(z.real))
        elif z.real<0:
            theta=m.atan(float(z.imag)/float(z.real))+m.pi
        else:
            theta=m.pi if z.imag > 0 else 3./2.*m.pi
        ret.append( abs(z)*m.e**((theta+rotate)*1j) )
    
    return ret
    

def make_center(S):
    r = [z.real for z in S]
    c = [z.imag for z in S]

    r_center = (min(r)+max(r))/2.
    c_center = (min(c)+max(c))/2.

    return [z.real-r_center + (z.imag-c_center)*1j for z in S]
