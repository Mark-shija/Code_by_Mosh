numbers = [1, 2, 3, 4, 5, 6, 7]
#  list packing
first, second, *other = numbers
print(second)
print(other)
#  unpckinng trick
# for unpacking to work the number of variable to be created mus be == list items
first, second, third, fourth, fiveth, sixth, seventh = numbers

# numbers[0] = 1
# numbers[1] = 2
# numbers[2] = 3
# ...........


for number in numbers:
    print(number)
