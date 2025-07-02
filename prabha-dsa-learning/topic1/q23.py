# Read the last index of even number

arr =[1,3,5,7,9,2,4,6,8,11]

for i in range(len(arr)- 1, -1, -1):
    if arr[i] % 2 ==0:
        print("Index of last even number", i)
        break
else:
    print("no even numbers")

