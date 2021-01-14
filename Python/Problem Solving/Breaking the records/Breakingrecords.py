#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mi=scores[0]
    ma=scores[0]
    l1=[]
    l2=[]
    for i in range(len(scores)):
        if scores[i]>ma:
            ma=scores[i]
            l1.append(scores[i])
        elif scores[i]<mi:
            mi=scores[i]
            l2.append(scores[i])
    return (len(l1),len(l2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
