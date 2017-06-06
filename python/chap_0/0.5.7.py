#!/usr/bin/env python
# -*- coding: utf-8 -*-

a={3,4,5}
b={5,6,7}
ret = {x*y for x in a for y in b}
print ret

