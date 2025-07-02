# Read last event elements in the given array
arr = [11,15,21,18,27,33,40,50,60,70]

# Flag to check if even number is found
found = False
# Found through array to find last even number

# reversed() is used to reverse the order of the elements in the array
for number in reversed(arr):
    if number%2 == 0:
        print("Last elements is ",number)
        found = True
        break
if not found:
    print("No even number found in the array")
