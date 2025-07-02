# Index of the first even elemenst in the given array

arr = [3,5,7,8,9,10,11,13,15,17,19]

# Count for even numbers
even_count = 0
# Loop to find index of 2nd number 
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_count += 1
        if even_count  == 2:
            print("Index of second even numebr is",i)
            break
else:
    print("Less than 2 even number")
