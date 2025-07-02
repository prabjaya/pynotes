# Read second even elements in the given array

arr = [1,4,7,8,10,11,13,14,15,17]

# Loop through array to find second even number
count = 0

for number in arr:
    if number % 2 == 0:
        count += 1
        if count == 2:
            print("second element", number)
            break
else:
    print("no Elements")