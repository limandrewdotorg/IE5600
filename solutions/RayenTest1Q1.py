"""
Created on Fri Aug 21 18:06:50 2020

@author: rayen
"""

test = int(input())
if 1 <= test <= 100:
    for _ in range(test):
        n = int(input())
        A = [int(x) for x in input().split()]
        m = int(input())
        if m < 1 or m > 5:
            exit()
        B = [int(x) for x in input().split()]
        
        for b in B:
            candies = []
            for a in A.copy():
                if a % b == 0:
                    candies.append(a)
                    A.remove(a)
            if not candies:
                print(-1)
            else:
                print(" ".join([str(x) for x in sorted(candies)]))
        if not A:
            print(-1)
        else:
            print(" ".join([str(x) for x in sorted(A)]))