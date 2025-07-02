# Read third odd element in the given Array

arr = [2,3,5,8,11,13,14,15,16]


# Loop through array to find third odd number
count = 0
for number in arr:
    if number % 2 != 0:
        count +=1
        if count == 3:
            print("The third odd element is",number)
            break
else:
    print("No third odd number found in the given array")