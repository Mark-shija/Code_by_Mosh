def greet(name):
    print(f"Hi {name}")


greet("John")

#  Types of functions
# 1.functon that perform a certain task
# 2.function that can compute qand return a value


def get_greeting(name):
    return f" Hi! {name}"


greeting_message = get_greeting("John Smith")
print(greeting_message)
# file = open("context.txt" "w")
# file.write(greeting_message)

print(greet("John"))


def fn(n):
    """
    A function that calculates the square of a given number.
    """
    return n*n


total = fn(6)
print(total)
