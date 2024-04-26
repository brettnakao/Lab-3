#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:20:31 2024

@author: brettnakao
"""

"""List of prime numbers"""

list_prime = [1, 2, 3, 5, 7] #define list

list_prime.append(11) #additions
list_prime.append(13)

new_list = list_prime[:3] #takes first 3
print(new_list)

list_new_prime = [17, 19, 23]

list_prime.extend(list_new_prime) #add list_new_prime to list_prime

print(list_prime)

print(list_prime[::-1]) #reverse order of list

list_prime.reverse() #reverse order of list alternate code
print(list_prime)
