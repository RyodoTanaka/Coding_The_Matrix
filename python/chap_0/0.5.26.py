#!/usr/bin/env python
# -*- coding: utf-8 -*-

d={0:1000.0, 3:990, 1:1200.50}
L=['Larry', 'Curly', '', 'Moe']

ret = {L[k]:v for (k,v) in d.items()}
print ret
