#   in this file we are going to look on how we can access item in alist

#  we can use square braces  and indeces to access a list
letters = ["A", "B", "C"]

# using -1 indeces to access list from end to start of a list

print(letters[-1])

Matrix = [[0, 2], [1, 2]]

chars = letters[-1]
letters[-1] = "F"
print(chars)

print(Matrix[1])
print(Matrix[-2])

#  we an use for loop to iterate a list

for letter in letters:
    print(letter)

# Printing ordered list

count = list(range(30))
print(count)

# print list even lists
print(count[::2])

# print a list in reverse order
print(count[::-1])

#  list un-packing
numbers = [1, 2, 3]
First, Second, Third = numbers
for number in numbers:
    print(number)

# when doing list un-packing, number of variable should be  equal to list items in the list
numbers = [1, 2, 3, 4, 5, 6, 7]
First, Second, Third = numbers
for number in numbers:
    print(number)

#  the above code will result error due to exceeded number of items in the list
