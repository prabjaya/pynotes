# Read last four elements in the given array 

# Declare and initialoze the array
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# Access the last four elements using slicing[] ---> -4
# Slicing is used to get a sublist from the list
last_four_elemnts = numbers[-4:]

# print the result
print("Last four elemnts", *last_four_elemnts)
