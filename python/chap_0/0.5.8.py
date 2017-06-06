#!/usr/bin/env python
# -*- coding: utf-8 -*-

a={5,6,7}
b={2,3,4}
ret = {x*y for x in a for y in b if x*y<20}
print ret

