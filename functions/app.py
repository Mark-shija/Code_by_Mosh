def greet(name):
    print(f"Hi {name}")


greet("John")

#  Types of functions
# 1.functon that perform a certain task
# 2.function that can compute qand return a value
#  the below function can not print anything on the terminal, will return a value that can be stored in any variable


def get_greeting(name):
    return f" Hi! {name}"


greeting_message = get_greeting("John Smith")
print(greeting_message)
# file = open("context.txt" "w")
# file.write(greeting_message)

print(greet("John"))