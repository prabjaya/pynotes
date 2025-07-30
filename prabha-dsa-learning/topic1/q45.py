# Find biggest Element
arr = [5, 9, 2, 14, 8, 6, 12, 3, 10, 4]
max_element = arr[0]  

for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print("Biggest element:", max_element)