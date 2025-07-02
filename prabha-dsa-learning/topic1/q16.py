# Read last odd elements in the given array

arr = [2,4,6,8,10,11,13,15]

# flag to check if odd number is found
found = False

# loop through array to find last odd number
for number in reversed(arr):
    if number % 2 !=0:
        print("Last odd element is",number)
        found = True
        break
if not found:
    print("No add number found in the given array")