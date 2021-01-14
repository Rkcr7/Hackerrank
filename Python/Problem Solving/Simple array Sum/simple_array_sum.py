#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar_count,ar):
    #
    # Write your code here.
    c=0
    for i in range(0,ar_count):
        c+=ar[i]
    return (c)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar_count,ar)

    fptr.write(str(result) + '\n')

    fptr.close()