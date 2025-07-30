# Read 1st Half of an Even-Length Array in Reverse Order and Pick Alternate Elements 

# Declare and initialize the array
arr = [10, 20, 30, 40, 50, 60, 70, 80]

n = len(arr)

if n % 2 == 0:
    print("Alternate elements from 1st half in reverse order:")
    for i in range(n // 2 - 1, -1, -2):
        print(arr[i], end=" ")
else:
    print("Array does not have even number of elements.")
