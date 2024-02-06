#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:09:39 2024

@author: brettnakao
"""

import math

print("input x component")
x = float(input())

y = float(input("input y component: "))

vector = (x, y)

magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
