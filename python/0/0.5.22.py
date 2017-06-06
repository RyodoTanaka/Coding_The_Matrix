#!/usr/bin/env python
# -*- coding: utf-8 -*-

dlist=[{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]

k='Bilbo'
ret = [i[k] if k in i else 'NOT PRESENT' for i in dlist]
print ret

k='Frodo'
ret = [i[k] if k in i else 'NOT PRESENT' for i in dlist]
print ret
