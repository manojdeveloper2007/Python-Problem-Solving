# Write a program to calculate biggest & smallest of given  numbers using a logical operator

"""
Test Case 1 :                               Test Case 2 :
    I/P:                                        I/P:
        12                                          17
        14                                          12
        17                                          257

    O/P:                                        O/P:
        17  12                                        257  12

"""


def biggest(num1: int, num2: int, num3: int) -> int:
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3

    else:
        if num2 > num3:
            return num2

        else:
            return num3


def smallest(num1: int, num2: int, num3: int) -> int:
    if num1 < num2:
        if num1 < num3:
            return num1
        else:
            return num3

    else:
        if num2 < num3:
            return num2

        else:
            return num3


num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

bignum, smallnum = biggest(num1, num2, num3), smallest(num1, num2, num3)

print(f"Biggest : {bignum}\nSmallest : {smallnum}")
