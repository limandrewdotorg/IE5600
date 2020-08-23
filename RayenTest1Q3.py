# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:26:42 2020

@author: rayen
"""

test = int(input())
if test < 1 or test > 100:
    exit()
for _ in range(test):
    n = int(input())
    if n < 2 or n > 1000:
        exit()
    x = [int(i) for i in input().split()]
    #Implement your Code Here
    mini_distance = 10**6
    
    for i in range(n):
        for j in range(i+1, n):
            dist = x[i] - x[j]
            if abs(dist) < mini_distance:
                mini_distance = abs(dist)
    #Output Solution
    print(mini_distance)