# read first even elements in the given array

arr = [11,15,21,18,27,33,40,50,60,70]

# Flag to check if even number is found

found = False

# Found through array to find first even number
for number in arr:
    if number %2 == 0:
        print("first even element",number)
        found = True
        break
if not found:
    print("No even number found in the array")


