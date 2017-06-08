#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot(S, limit, plt_num=1):
    fig=plt.figure(plt_num)
    if isinstance(S[0], complex):
        plt.plot([cnum.real for cnum in S], [cnum.imag for cnum in S], 'ro')
    else:
        plt.plot([d[0] for d in S],[d[1] for d in S],'ro')
    plt.axis([-limit, limit, -limit, limit])
    plt.grid()

def quniver(start, cvector, limit, plt_num=1):
    fig=plt.figure(plt_num)
    if isinstance(start, complex) and isinstance(cvector, complex):
        plt.quiver(start.real, start.imag, cvector.real, cvector.imag ,angles='xy',scale_units='xy',scale=1)
    else:
        plt.quiver(start[0], start[1], cvector[0], cvector[1] ,angles='xy',scale_units='xy',scale=1)
    plt.axis([-limit, limit, -limit, limit])
    plt.grid()
    plt.draw()

def show():
    plt.show()
