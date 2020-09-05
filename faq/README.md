---
title: IE5600 FAQ
date: 2020-08-24 13:16:25
tags:
- IE5600
- FAQ
categories:
- IE5600 TA
---

# IE5600 FAQ

## Why do we need to use try/except?

Intersection of Two Arrays (P128) is the only problem that you need to use try/except. It is used to deal with the special case that we want the intersection of two empty arrays.

If the input array is empty, simply use a input() function will lead to the EOFError. Instead, we should use try/except like following:
```python
try:
	a = input()
except:
	a = ""
try:
	b = input()
except :
	b = ""
```

Many of you are also curious why we should print nothing in the except part. Actually, it is just because when the input is empty arrays, the intersection also happens to be an empty array. You can output nothing in the except part and exit your program, or you can write your code like above, and continue to do the computation.

I think many of you are confused about the input and output. In the following questions, we will make sure that there are no issues about I/O. So you can focus on algorithms. If you still get an Run Error, you may consider bugs like memory error in your code.

## Why do we need to use input().split() instead of input().split(" ")

The split() method splits a string into a list. split() function set the separator to be any whitespace. However, split(" ") will set the separator to be **excatly one whitespace**, which will lead to error when there are more than one consecutive spaces. The following example can help you understand.
```python
test1 = "1 2 3"
res1 = test1.split()
res2 = test1.split(" ")
# res1 = ["1","2","3"]
# res2 = ["1","2","3"]

test2 = "1  2 3"
# noted that there are 2 spaces between 1 and 2
res3 = test2.split()
res4 = test2.split(" ")
# res3 = ["1","2","3"]
# res4 = ["1","","2","3"]

list(map(int,res3))
# will return [1,2,3]
list(map(int,res4))
# will raise an error. Because you cannot apply int() function to empty string "".
```

## Why do I get wrong answer in P128 even I sorted the output

Noted that in some problems we need to sort the integers. Many submission are wrong because the sort function is applied on a list of string instead of a list of number. The following example can help you understand.
```python
list1 = ["11","2","3","111"]
list1.sort()
# list1 is ['11', '111', '2', '3']

list2 = ["11","2","3","111"]
list2 = [int(i) for i in list2]
# list2 = [11,2,3,111]
list2.sort()
# list2 is [2,3,11,111]
```

## How to output for problems in Test1?

Noted that in the problems of Test1, the input, which include multiple cases in one sample, is a bit different from previous problems. Many students struggle to format the output and print at the end of the program. Actually, you can output inside the "for" loop every time you get an answer.  The code for P163 can help you understand.

```python
#P163
test = int(input())
for _ in range(test):
    l,x,T = map(int,input().split())
    #Implement your code here
    k=T%(2*l)
    if k<=l-x:
        position = x+k 
    else:
        position = abs(2*l-k-x)
    #Output Solution
    print(position)
```

## Some resources about python

In order to improve your python ability quickly, you may refer to the following resources.

- [W3school](https://www.w3schools.com/python) has a tutorial related to python grammar. There are also some [exercises](https://www.w3schools.com/python/exercise.asp) for you.  
- If you would like to read more codes in python, you may refer to [Github](https://github.com/).




## Min and the second Min element in array

Divide and conquer gives a tournament style solution to find the min element in array:

```python
import random

def minandmax(arr, l, r):
    if r - l + 1 <= 2:
        return (min(arr[l],arr[r]), max(arr[l],arr[r]))
    mid = (l+r) // 2
    arr1min, arr1max = minandmax(arr, l, mid)
    arr2min, arr2max = minandmax(arr, mid+1, r)
    return (min(arr1min, arr2min), max(arr1max, arr2max))
a = [62, 94, 11, 91, 90, 15, 40, 53, 56, 70, 55, 5, 20, 10, 8, 37, 19, 50, 93, 10]
print(a)
print(minandmax(a, 0, a.__len__() - 1))
```



When the Min element is found, the Min beats $\log n$ elements, find the min element among these will be the answer

```python
def minandsecondmin(arr, l, r):
    if r - l + 1 <= 2:
        return min(arr[l],arr[r]), [max(arr[l], arr[r])]
    mid = (l+r) // 2
    arr1min, listl = minandsecondmin(arr, l, mid)
    arr2min, listr = minandsecondmin(arr, mid+1, r)
    if arr1min < arr2min:
        return arr1min, listl + [arr2min]
    else:
        return arr2min, listr + [arr1min]
a = [62, 94, 11, 91, 90, 15, 40, 53, 56, 70, 55, 5, 20, 10, 8, 37, 19, 50, 93, 10]
print(a)
Min, Smin = minandsecondmin(a, 0, a.__len__() - 1) #On time
print(Min, Smin)
print(min(Smin)) #logn time


```

## Python Recursive depth limit
Python have internal recursive depth limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. If you write a function that runs recursively, this limit may be exceeded. In that case, you need to remove this limit by:

```
import sys
sys.setrecursionlimit(your_estimated_upper_bound)

```



