# read first five elememts and last two elements in the given array


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Access the first two elements using slicing
first_five_elements = numbers[:5]
# Access the last two elements using slicing
last_two_elements = numbers[-2:]

# print the result
print("first five elements", *first_five_elements)
print("last two elements", *last_two_elements)
