#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vector_plot as vplt

L=[ [2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1] ]
limit=4

vplt.plot2d([[d[0]+1,d[1]+2] for d in L ], limit, 1)
vplt.show()

