# Read all even and odd elements in the given array

arr = [1,2,3,4,5,6,7,8,9,10]

total = len(arr)
even_count = 0
odd_count = 0
# loop through count odd and even elements
for number in arr:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display list
print("Total number of elements", total)
print("Total number of odd elements", odd_count)
print("Total number of even elements",even_count)

