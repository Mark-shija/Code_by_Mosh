items = [
    ("product1", 10),
    ("product2", 30),
    ("product3", 20),
    ("product4", 12)
]

#  like map function, Filter function return an filter object

# filtered = filter(lambda item: item[1] >= 10, items)

""" list compliation on line 10"""
[item[1] for item in items if item[1] >= 10]

# print(filtered)
# for item in filtered:
#     print(item)

# u can use list method

filtered = list(filter(lambda item: item[1] >= 20, items))
""" List compliations"""
price = [item[1] for item in items if item[1] >= 10]
print("Price of each product in the list are as follows: ")
print(price)
