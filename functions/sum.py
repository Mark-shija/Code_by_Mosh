def sum(num1, num2):
    return num1 + num2


result = sum(10, 20)
print(result)


# using keyword argument in python functions
def increment(number, by):
    return number + by


print(increment(10, by=40))

# making second argument optional when invoking the function


def increment(number, by=5):
    return number + by


print(increment(2))

# working with xargs in py


def sum(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


resulting_total = sum(1, 2, 3, 4, 5)
print(resulting_total)


def fn(n):
