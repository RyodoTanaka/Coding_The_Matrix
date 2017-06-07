#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot(S, limit):
    rpoints=[cnum.real for cnum in S]
    cpoints=[cnum.imag for cnum in S]
    plt.plot(rpoints, cpoints, 'ro')
    plt.axis([-limit, limit, -limit, limit])
    plt.grid()

def quniver(start, cvector, limit):
    plt.quiver(start.real, start.imag, cvector.real, cvector.imag ,angles='xy',scale_units='xy',scale=1)
    plt.axis([-limit, limit, -limit, limit])
    plt.grid()
    plt.draw()

def show():
    plt.show()
