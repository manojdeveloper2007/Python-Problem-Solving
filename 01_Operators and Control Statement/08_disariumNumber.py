# Write a program to check whether the number is Disarium Number or not ?
#  --- Example ., 175-> 1**1 + 7**2 + 5 ** 3 = 175

"""
Test Case 1 :                       Test Case 2 :
    I/P :                               I/P :
        175                                1634

    O/P :                               O/P :
        Disarium Number                           Not Disarium Number

"""


def countDigit(num: int) -> int:
    cnt = 0

    while num > 0:
        cnt += 1
        num //= 10

    return cnt


def isDisarium(num: int) -> int:
    sum = 0
    count = countDigit(num)

    temp = num

    while temp > 0:
        sum += (temp % 10) ** count
        temp //= 10
        count -= 1

    return sum == num


num = int(input("Enter the Number : "))

if isDisarium(num):
    print("Disarium number")

else:
    print("Not disarium number")
