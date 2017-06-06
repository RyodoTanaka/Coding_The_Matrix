#!/usr/bin/env python
# -*- coding: utf-8 -*-

S={-4,-2,1,2,5,0}

ret = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i!=0 or j!=0 or k!=0)][0]
print ret

