# read first two elememts and last five elements in the given array


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Access the first two elements using slicing
first_two_elements = numbers[:2]
# Access the last two elements using slicing
last_five_elements = numbers[-5:]

# print the result
print("first two elements", *first_two_elements)
print("last five elements", *last_five_elements)
