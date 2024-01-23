#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps = 0
    for i in range(0, len(a), 1):
        for j in range(0, len(a) -1, 1):
            if(a[j]>a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swaps += 1
        if swaps == 0: break
    
    print(f'Array is sorted in {swaps} swaps.')
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")

    print(a)