# Declare and initialize the array
arr = [10, 20, 15, 25, 5, 30]

print("Indexes where element is greater than both neighbors:")
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(i, end=" ")