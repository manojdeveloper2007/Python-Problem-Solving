# Write a Program to find the given number is a prime palindrome or not

"""
Test Case 1 :                               Test Case 2 :
    I/P:                                        I/P:
        100                                         191
    O/P:                                        O/P:
        Not prime palindrome                         prime palindrome

"""


def isPalindrome(num) -> bool:
    temp = num

    reverse = 0

    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10

    return reverse == num


def isPrime(num) -> bool:
    for i in range(2, num // 2):
        if num % i == 0:
            return False

    return True


num = int(input("Enter Number : "))

if isPalindrome(num) and isPrime(num):
    print("Prime Palindrome")

else:
    print("Not prime palindrome")
