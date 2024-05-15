list = [1, 2, 3, 4, 5]

# enumerate function return tuples

for item in enumerate(list):
    print(item)

letters = ["a", "b", "c", "d"]

#  append method will add new list item at the end of the list
letters.append("e")
print(letters)

# Insert method will add new member at the beginning of the list
#  The method takes index and new list member name
letters.insert(0, "Victoria")
print(letters)

# REMOVE item at the end of the list
print(letters)
letters.pop()
print(letters)

#  remove items in allist at specified index
letters.pop(0)
print(letters)
#  you an name the itemin the list you want to eliminate
#  this will remove the first occurance in the list

# letters.remove("c")
letters.append("h")
print(letters)
del letters[1:3]
print(letters)

# we use clear method when we want to remove all items in the list
# letters.clear()
# print(letters)


#  getting the index of the list
#  it is better to check if an item is present in the list
#  before we finf or search its index
if "d" in letters:
    print(letters.index("g"))
