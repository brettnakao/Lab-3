#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:09:39 2024

@author: brettnakao
"""

"""Vector Tuple""" # Title code

import math

x = float(input("Enter x component:")) # Define x value
y = float(input("Enter y component:")) # Define y value

vector = (x, y) # Define vector

magnitude = math.sqrt(vector[0]**2 + vector[1]**2) # Define magnitude
