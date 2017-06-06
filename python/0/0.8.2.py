#!/usr/bin/env python
# -*- coding: utf-8 -*-

def inv_dict(d):
    return {v:k for (k,v) in d.items()}

d={'thank you': 'merci', 'good bye':'au revoir'}

print inv_dict(d)
