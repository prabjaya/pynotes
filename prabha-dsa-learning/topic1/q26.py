# Index of last third odd number in the given elememts
arr = [1,3,5,7,2,4,6,8,9,11]

count = 0 


for i in range(len(arr)-1, -1, -1):
    if arr[i] % 2 != 0:
        count += 1
        if count == 3:
            print("Index of last 3'r number", i)
            break
else:
    print("less than 3 odd number found")


