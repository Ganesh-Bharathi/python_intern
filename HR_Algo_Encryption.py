import math
import os
import random
import re
import sys
import numpy as np
import itertools

"""
# Complete the encryption function below.
def encryption(s):
    
    l=len(s)
    a=float(l**0.5)
    # print(a)
    lo=int(a)
    up=int(a)+1
    if (lo*up)<l:
        lo=up
    # print(lo)
    # print(up)
    lis=[]
    j=0
    k=up
    for i in range(lo):
        lis.append((list(s[j:k])))
        j+=up
        k=k+up
    print(lis)
    if len(lis[lo-1]) != len(lis[lo-2]):
        n=len(lis[lo-2])-len(lis[lo-1])
        for i in range(n):
            lis[lo-1].append('0')
    # print(lis)
    ar=np.array(lis)
    # print(ar)
    ar=ar.T
    # print(ar)
    lis = list(ar)
    lis=list(map(list,lis))
    # print(lis)
    for i in range(up):
        if lis[i][lo-1]=='0':
            del(lis[i][lo-1])
    print(lis)
    for i in lis:
        print((''.join(i)),end=' ')
"""


"""
def encryption(s):
    
    l=len(s)
    a=float(l**0.5)
    # print(a)
    lo=int(a)
    up=int(a)+1
    if (lo*up)<l:
        lo=up
    # print(lo)
    # print(up)
    lis=[]
    j=0
    k=up
    for i in range(lo):
        lis.append((list(s[j:k])))
        j+=up
        k=k+up
    print(lis)

    # a=list(map(list,zip(*lis)))
    # print(a)
    a=(itertools.zip_longest(*lis, fillvalue=''))
    a=list(map(list,a))
    print(a)
    # for i in range(up):
    #     if a[i][lo-1]==None:
    #         del(a[i][lo-1])
    # print(a)
    # if len(lis[lo-1]) != len(lis[lo-2]):
    #     n=len(lis[lo-2])-len(lis[lo-1])
    #     for i in range(n):
    #         lis[lo-1].append('0')
    # # print(lis)
    # ar=np.array(lis)
    # # print(ar)
    # ar=ar.T
    # # print(ar)
    # lis = list(ar)
    # lis=list(map(list,lis))
    # # print(lis)
    # for i in range(up):
    #     if lis[i][lo-1]=='0':
    #         del(lis[i][lo-1])
    # print(lis)
    for i in a:
        print((''.join(i)),end=' ')

"""

""" a = [['1'], ['2'], ['3'], ['4'], ['5']]
# b = str(a)
# b=""
for i in a:
    # for j in i:
        # b=b+j
    print(''.join(i), end=' ')
# print(b) """

s = input()
encryption(s)