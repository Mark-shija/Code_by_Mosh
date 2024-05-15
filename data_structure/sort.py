#  sort method is used to sort list items in ascending order

numbers = [30, 12, 45, 2, 20, 1, 4, 6, 3]
# numbers.sort()
# print(numbers)

# sort method can takes 2 arguments
# numbers.sort(reverse=True)

print(sorted(numbers, reverse=False))


items = [
    ("product1", 10),
    ("product2", 30),
    ("product3", 20),
    ("product4", 12)
]


""" sorting function
that will be taken as key in sorting method

"""


def sort_items(product):
    return product[1]


""" A method that prints sorted items list tuple"""
items.sort(key=sort_items, reverse=True)
print(items)

# we can use  lambda function toachieve the similar results

# lambda(parameters:expression)

items.sort(key=lambda product: product[1])
print(items)
