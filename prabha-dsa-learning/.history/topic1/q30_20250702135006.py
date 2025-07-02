# Declare and initialize the array
arr = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11]

# Part 1: Index of last 3rd odd number
odd_count = 0
odd_index_found = False

for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 2 != 0:
        odd_count += 1
        if odd_count == 3:
            print("Index of last 3rd odd number:", i)
            odd_index_found = True
            break

if not odd_index_found:
    print("Less than 3 odd numbers found")

# Part 2: Index of first even number
even_index_found = False

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print("Index of first even number:", i)
        even_index_found = True
        break

if not even_index_found:
    print("No even number found")