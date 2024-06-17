# Explore the difference between function parameters and Arguments
# we will use previous example from greeting.py  file

def greet(first_name, last_name):
    print(f"Hi! {first_name} {last_name}")
    print("Welcome to my Github Account")
    print("Tell me if I make progress in coding")

greet("John", "Smith")

try:
    Message = str(input("Type your conversation here: "))
except ValueError:
    print('you did not provide any message!!')
else:
    print("No any Exception were thrown")
print(Message)
