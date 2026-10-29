# Write the recursive function to find factorial of number


def factorial(num: int):

    if num <= 1:
        return 1

    return num * factorial(num - 1)


num = int(input("Enter Number : "))
print(factorial(num))
