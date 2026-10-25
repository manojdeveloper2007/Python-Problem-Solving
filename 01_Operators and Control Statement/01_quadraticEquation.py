#   1 . Write a program to calculate the roots of a quadratic equation

"""
Test Case 1 :                               Test Case 2 :
    I/P:                                        I/P:
        1                                           1
        -9                                         -6
        20                                          9

    O/P:                                        O/P:
        5  4                                        3  3
"""

import math


def quadraticEquation(a: int, b: int, c: int):

    formula_1 = int((-b + math.sqrt((b**2) - 4 * a * c)) // (2 * a))
    formula_2 = int((-b - math.sqrt((b**2) - 4 * a * c)) // (2 * a))

    return formula_1, formula_2


a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : "))

root_1, root_2 = quadraticEquation(a, b, c)

print(f"Root 1 = {root_1} \nRoot 2 = {root_2}")
