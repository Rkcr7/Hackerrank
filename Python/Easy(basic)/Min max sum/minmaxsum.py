#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    asc=sorted(arr)
    m=0
    for i in range(0,len(arr)-1):
        m+=asc[i]
    desc=sorted(arr,reverse=True)
    n=0
    for j in range(0,len(arr)-1):
        n+=desc[j]
    print(m,n)
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
