# Write a program to find the given number is neautiful or not

#   34 -> 3^2 + 4 ^2 = 9 + 16 = 25 = 5^2

"""
Test Case 1 :                       Test Case 2 :
    I/P :                               I/P :
        474                                 57

    O/P :                               O/P :
        Beautiful                           Not Beautiful

"""

import math


def isBeautiful(num: int) -> bool:
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem**2
        num = num // 10

    return math.sqrt(sum) % 1 == 0


num = int(input("Enter the Number : "))

if isBeautiful(num):
    print("Beautiful")
else:
    print("Not Beautiful")
