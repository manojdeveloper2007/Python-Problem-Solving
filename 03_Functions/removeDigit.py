# write a program to remove particular digit from the number


def removeDigit(number, digit):
    num = str(number)
    temp = [i for i in num if i != str(digit)]
    sum = 0

    for i in temp:
        sum = (sum * 10) + int(i)

    return sum


number = int(input("Enter Number : "))
digit = int(input("Enter Digit : "))
print(removeDigit(number, digit))
