# Indexes where element is greater than  it's right nighbour element.

arr = [10, 20,15,25,5,30]
print("Indexes where element is greater than  it's right nighbour element.")
for i in range(len(arr)-1):
    if(arr[i] > arr[i + 1]):
        print(i, end= " ")
        
