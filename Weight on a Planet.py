#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:33:26 2024

@author: brettnakao
"""

gravity = {"Earth": 9.8, "Mars": 3.75, "Mercury": 3.61, "Venus": 8.83, "Jupiter": 26.0, "Saturn": 11.2, "Uranus": 10.5, "Neptune": 13.3, "Pluto": 0.61}

print('What is your mass? ')
m = float(input())

print('What planet are you on? ')

p = input()

g = float(gravity[p])

x = float(m*g)

print('You weigh ' + str(x) + " N" + " on planet " + p + "!")