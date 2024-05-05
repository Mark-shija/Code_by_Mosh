# This code defines a function Fizz_Buzz that returns
# "Fizz" if the input is divisible by 3,
# "Buzz" if divisible by 5,
# "Fizz_Buzz" if divisible by both 3 and 5,
# and returns the input itself if not divisible by either.

def Fizz_Buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz_Buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(Fizz_Buzz(15))
