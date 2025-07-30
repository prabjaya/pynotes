# Read alternative elements in the given array from last elements
arr = [10,20,30,40,50,60,70,80,90,100]

print("Alternative elements in the reverse order")

for i in range(len(arr) -1, -1, -2):
    print(arr[i],end= " ")
