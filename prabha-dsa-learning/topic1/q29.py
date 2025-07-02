# Declare and initialize the array
arr = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11]

# Counter for odd numbers
count = 0

# Traverse array in reverse to find 3rd last odd number
for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 2 != 0:
        count += 1
        if count == 3:
            print("Index of last 3rd odd number:", i)
            break
else:
    print("Less than 3 odd numbers found")