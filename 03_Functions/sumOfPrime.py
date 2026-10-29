# write a function,to check whether the number can be expressed as sum of the prime numbers

"""
Test Case 1:                Test Case 2:
    I/P:                        I/P:
        20                          17
    O/P:                        O/P:
        True                        False
"""

import math


def isPrime(num: int) -> int:
    sum = 0
    temp = num
    while temp > 0:
        sum += temp % 10
        temp //= 10

    if sum <= 2:
        return False

    for i in range(2, sum // 2):
        if sum % i == 0:
            return True

    return False


num = int(input("Number : "))
print(isPrime(num))
