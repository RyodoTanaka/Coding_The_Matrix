#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_function_composition(f, g):
    return {fk:g[fv] for fk,fv in f.items()}

f={0:'a', 1:'b'}
g={'a':'apple', 'b':'banana'}

print my_function_composition(f, g)
