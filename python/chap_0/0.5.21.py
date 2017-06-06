#!/usr/bin/env python
# -*- coding: utf-8 -*-

dlist=[{'James':'Sean','director':'Terence'},{'James':'Roger','director':'Lewis'},{'James':'Pierce','director':'Roger'}]
k='James'
ret = [i[k] for i in dlist]
print ret

k='director'
ret = [i[k] for i in dlist]
print ret
