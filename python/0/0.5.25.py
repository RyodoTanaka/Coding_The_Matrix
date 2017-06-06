#!/usr/bin/env python
# -*- coding: utf-8 -*-

base=10
digits=set(range(base))

ret = {k:(k/(base**2)%base,k/(base)%base,k%base) for k in range(1000)}
print ret

base=2
ret = {k:(k/(base**2)%base,k/(base)%base,k%base) for k in range(8)}
print ret
