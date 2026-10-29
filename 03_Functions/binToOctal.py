# write a function to convert binary to ocatl number

"""
Test Case 1:                Test Case 2:
    I/P:                        I/P:
        11001                       1001001
    O/P:                        O/P:
        31                          111
"""


def binaryToOctal(num: int) -> bool:
    cnt = 0
    temp = num
    sum = 0
    l = []

    while temp > 0:
        if cnt != 0 and cnt % 3 == 0:
            cnt = 0
            l.append(sum)
            sum = 0
        p = 2**cnt
        rem = temp % 10
        sum += p * rem
        temp //= 10
        cnt += 1

    if cnt > 0:
        l.append(sum)

    sum = 0
    for i in range(len(l) - 1, -1, -1):
        sum = (sum * 10) + l[i]

    return sum


binary = int(input("Enter Binary Number : "))
print(binaryToOctal(binary))
