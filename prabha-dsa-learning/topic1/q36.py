# Read alternate elements from an array in Reverse order from second last elemnts

arr = [10,20,30,40,50,60,70,80,90,100]

print("Alternate elemnts in reverse order from second last elememts")
for i in range(len(arr)-2,-1,-2):
    print(arr[i], end= " ")
