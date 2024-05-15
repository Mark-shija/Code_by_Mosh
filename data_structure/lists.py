# list is defined using square braces

letters = ["A", "B", "C"]
print(letters)


# We can create a list of a list

Matrix = [[0, 2], [1, 2]]
print(Matrix)

# we use * sign to repeat an item in a list

number = [0, 0, 0, 0, 0, 0]
number_repeated = [0] * 6
print(number)
print(number_repeated)


# we use + sign to combine two or more lists
combined = letters + number_repeated
print(combined)


# we use list function or method to create a list

chars = list("Hello World")
print(chars)


count = list(range(30))
# range function will take all number in between 0-30, 30 exclusive
print(count)


# we use len() to print the length of the list, this counts individual  items in a list

print(len(count))
