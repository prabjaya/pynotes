# # Declare and initialize the array
arr = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11]

# Counter for even numbers
count = 0

# Loop in reverse to find second last even number
for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 2 == 0:
        count += 1
        if count == 2:
            print("Index of last 2nd even number:", i)
            break
else:
    print("Less than 2 even numbers found")
