#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot2d(L,  limit, plt_num=1):
    fig=plt.figure(plt_num)
    x=[d[0] for d in L]
    y=[d[1] for d in L]
    plt.plot([d[0] for d in L],[d[1] for d in L],'ro')
    plt.axis([-limit, limit, -limit, limit])
    plt.grid()

def show():
    plt.show()
