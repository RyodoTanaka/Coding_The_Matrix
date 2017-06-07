#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot(S, limit):
    rpoints=[cnum.real for cnum in S]
    cpoints=[cnum.imag for cnum in S]
    plt.plot(rpoints, cpoints, 'ro')
    plt.axis([-limit, limit, -limit, limit])
    plt.show()
