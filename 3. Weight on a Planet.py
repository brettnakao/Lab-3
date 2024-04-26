#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:33:26 2024

@author: brettnakao
"""

"""Mass on a Planet"""

#define gravity dictionary
gravity = {"Earth": 9.8, "Mars": 3.75, "Mercury": 3.61, "Venus": 8.83, "Jupiter": 26.0, "Saturn": 11.2, "Uranus": 10.5, "Neptune": 13.3, "Pluto": 0.61}

mass = float(input("Enter your mass in kg:"))
planet = input("Enter your desired planet:")

weight_on_planet = mass * gravity[planet] #define weight on desired planet

print("Weight on planet:", weight_on_planet, "N") #create string to print answer
