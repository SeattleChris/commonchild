#!/bin/python3

import os

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    n=len(s1) + 1  # The s1 and s2 are equal length strings
    m = [[0] * n for _ in range(n)]
    for a, va in enumerate(s1):
        for b, vb in enumerate(s2):
            if va ==vb:
                m[a+1][b+1]=max(m[a][b]+1,m[a+1][b-1])
                continue
            m[a+1][b+1]=max(m[a+1][b],m[a][b+1])
    return m[-1][-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()
