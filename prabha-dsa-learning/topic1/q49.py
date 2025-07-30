# Read biggest odd number in the given elements
arr = [5, 9, 2, 14, 7, 6, 13, 3, 10, 4]
max_odd = None

for num in arr:
    if num % 2 != 0:
        if max_odd is None or num > max_odd:
            max_odd = num

if max_odd is not None:
    print("Biggest odd element:", max_odd)
else:
    print("No odd element found")



