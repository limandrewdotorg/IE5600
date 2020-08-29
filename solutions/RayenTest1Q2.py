"""
Created on Fri Aug 21 20:26:42 2020

@author: rayen
"""

test = int(input())
for _ in range(test):
    l,x,T = map(int,input().split())
    #Implement your code here
    velocity = 1
    position = x
    for i in range(T):
        position += velocity
        if position == l or position == 0:
            velocity *= -1
    #Output Solution
    print(position)