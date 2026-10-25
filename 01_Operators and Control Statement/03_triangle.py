# Write a program to check whether a triangle is Equilateral , Isosceles or Scalene

"""
Test Case 1 :                               Test Case 2 :
    I/P:                                        I/P:
        12                                          17
        12                                          12
        12                                          17

    O/P:                                        O/P:
        Equilateral                                  Isosceles

"""


def is_Equilateral(base, height, hypotenuse) -> bool:
    return base == height == hypotenuse


def is_Isosceles(base, height, hypotenuse) -> bool:
    return base == height or height == hypotenuse or base == hypotenuse


def is_Scalene(base, height, hypotenuse) -> bool:
    return base != height != hypotenuse


base = int(input("Enter Base : "))
height = int(input("Enter Height : "))
hypotenuse = int(input("Enter Hypotenuse : "))

if is_Equilateral(base, height, hypotenuse):
    print("Equilateral")

elif is_Isosceles(base, height, hypotenuse):
    print("Isosceles")

else:
    print("Scalene")
