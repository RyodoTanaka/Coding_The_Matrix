#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

L=[ [2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1] ]
x=[d[0] for d in L]
y=[d[1] for d in L]
limit=4

plt.plot(x,y,'ro')
plt.axis([-limit, limit, -limit, limit])
plt.grid()
plt.show()
