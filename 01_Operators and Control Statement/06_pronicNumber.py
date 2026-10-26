# Write a program to check whether the number is pronic or not

# ----- Example : 42 = 6 * 7 , If the divisors are consecutive ,then it is pronic number

"""
Test Case 1 :                   Test Case 2 :
    I/P:                            I/P:
        42                              45

    O/P:                            O/P:
        Pronic Number                   Not Pronic Number
"""


def isPronicNumber(num: int) -> int:
    for i in range(2, num // 2 + 1):
        if i * (i + 1) == num:
            return True

        if i * (i + 1) > num:
            return False


num = int(input("Enter The Number : "))

if isPronicNumber(num):
    print("Pronic Number")

else:
    print("Not Pronic Number")
