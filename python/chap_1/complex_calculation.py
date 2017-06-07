#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m

def rotate(S, rotate):
    return [abs(z)*m.e**( ( m.atan(float(z.imag)/float(z.real)) + rotate ) * 1j ) if z.real!=0 else abs(z)*m.e**(rotate*1j) for z in S]
