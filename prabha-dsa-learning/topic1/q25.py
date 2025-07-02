# index of last second even number
arr = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11]
count = 0

# Loop in reverse to find index of second last even number
for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 2 == 0:
        count += 1
        if count == 2:
            print("Index of second last even number is", i)
            break
else:
    print("Less than 2 even numbers")
