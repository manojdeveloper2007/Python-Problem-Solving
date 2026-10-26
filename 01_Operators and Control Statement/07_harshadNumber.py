# Write a program to check whether the number is Harshad Number or not ?

# ---- Example --> 171 - Sum of digits = 9 ,171 exactly divisible by 9,then it is harshad number

"""
Test Case 1 :                       Test Case 2 :
    I/P :                               I/P :
        171                                1634

    O/P :                               O/P :
        Harshad Number                           Not Harshad Number

"""


def isHarshadNumber(num: int) -> bool:
    sum = 0
    temp = num

    while temp > 0:
        sum += temp % 10
        temp //= 10

    return num % sum == 0


num = int(input("Enter the Number : "))

if isHarshadNumber(num):
    print("Harshad Number")

else:
    print("Not Harshad Number")
