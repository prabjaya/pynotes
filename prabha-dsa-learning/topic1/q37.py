# Read 2'd half of an elements in reverse order

arr=[10,20,30,40,50,60,70,80]

n = len(arr)
if n % 2 == 0:
    print("Second half elements in reverse order")
    for i in range(n - 1,n // 2 -1,-1):
        print(arr[i],end= " ")   
else:
    print("Array does not have number")

