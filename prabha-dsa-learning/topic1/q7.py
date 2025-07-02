# Read first 5 elements in the given array
# declare and initialize the array
numbers = [10,20,30,40,50,60,70,80,90,100]

# Access the first 5 elemnts uisng slicing[]  ---> 0 is inclusive and 5 is exclusive
# Slicing is used to get a sublist from the list
first_five_elements = numbers[:5]

# print the result
print("first five elements",*first_five_elements)
# output
# first five elements 10 20 30 40 50
print("first five elements",first_five_elements)
# output
# first five elements [10, 20, 30, 40, 50]
