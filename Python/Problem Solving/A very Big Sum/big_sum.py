#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar_count,ar):
    x=0
    for i in range(ar_count):
        x+=ar[i]
    return(x)
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar_count,ar)

    fptr.write(str(result) + '\n')

    fptr.close()
