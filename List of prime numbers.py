#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:20:31 2024

@author: brettnakao
"""

prime = [1, 2, 3, 5, 7]


prime.append(11) #additions
prime.append(13)
prime.append(17)
prime.append(19)

prime_first = prime[0] #first in the list

prime_last = prime[-1] #last in the list

new_prime = prime[0:3] #new list with first three

new_prime_2 = prime[3:7]

combined_prime_numbers = new_prime + new_prime_2

combined_prime_numbers.reverse()