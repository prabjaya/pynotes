# Read first odd elememts from the give array

arr = [2,4,6,7,8,10,11,13,15,17]

# Loop to find the first odd number
for number in arr:
    if number % 2 !=0:
        print(number)
        break
else:
    print("No odd number found")