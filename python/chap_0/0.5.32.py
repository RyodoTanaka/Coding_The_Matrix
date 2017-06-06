#!/usr/bin/env python
# -*- coding: utf-8 -*-

def all_3_digit_numbers(base, digits) : return {a*(base**2)+b*base+c for a in digits for b in digits for c in digits}

print all_3_digit_numbers(2,{0,1})
print all_3_digit_numbers(3,{0,1,2})
print all_3_digit_numbers(10,{0,1,2,3,4,5,6,7,8,9})
