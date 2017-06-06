#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

for i in range(3):
    print randint(0,1000)

def movie_review(name) : return ('See it !', 'A gem !', 'Ideological claptrap !')[randint(0,2)]

print movie_review('Star Wars')
print movie_review('Sin GodZilla')
print movie_review('Catch me if you can')
print movie_review('Evangelion')
