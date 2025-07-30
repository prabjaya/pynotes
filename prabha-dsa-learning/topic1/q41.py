# Declare and initialize the array
arr = [2, 3, 5, 1, 4, 6, 8, 2]

print("Indexes where three consecutive elements are increasing:")
for i in range(len(arr) - 2):
    if arr[i] < arr[i + 1] and arr[i + 1] < arr[i + 2]:
        print(i, end=" ")