import math
import os
import random
import re
import sys


def numTable(n):
    i = 1
    while(i<11):
        p = n*i
        print(n,"x",i,"=",p)
        i+=1


if __name__ == '__main__':
    n = int(input().strip())
    numTable(n)
