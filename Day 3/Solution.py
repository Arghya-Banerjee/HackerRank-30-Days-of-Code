import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    sum = 0
    
    sum = sum + meal_cost
    tip_amt = meal_cost * (tip_percent/100)
    tax_amt = meal_cost * (tax_percent/100)
    
    sum = sum + tip_amt + tax_amt
    
    print(round(sum))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)