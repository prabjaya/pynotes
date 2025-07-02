# Index of last odd number

arr = [2,4,6,8,10,11,13,15,17,20]

# Loop inreverse to find index of last odd number

for i in range(len(arr)- 1, -1, -1):
    if arr[i] % 2 !=0:
        print("Index of last odd number", i)
        break
else:
    print("no odd numbers")
