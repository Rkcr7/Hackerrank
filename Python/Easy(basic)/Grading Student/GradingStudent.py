#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final=[]
    
    # Write your code here
    for i in range(len(grades)):
        r=round(grades[i]/5)*5
        s=r-grades[i]
        if grades[i]<38:
            final.append(grades[i])
        elif grades[i]>=38:
            
            if s<0:
                final.append(grades[i])
            elif s>0:
                final.append(r)
            else:
                final.append(grades[i])
    return(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
