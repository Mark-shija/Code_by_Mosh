list1 = [1, 2, 3, 4, 5]

list2 = [10, 30, 40, 50, 60]

list3 = list1 + list2
print(list3)

""" zip function or method returns tuple of multiple lists"""
list4 = zip("abcde", list1, list2)
print(list(list4))
