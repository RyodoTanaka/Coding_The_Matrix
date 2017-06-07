#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cplotting as cplot
import complex_calculation as ccalc
import math as m

S={2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

cplot.plot(ccalc.rotate(S, 1./4.*m.pi),4)
cplot.show()
