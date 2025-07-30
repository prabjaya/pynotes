# Get smallest number in the given elements.
arr = [5, 9, 2, 14, 8, 6, 12, 3, 10, 4]

min_element = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]

print("Smallest element:", min_element)