# Read Smallest odd element
arr = [5, 9, 2, 14, 7, 6, 13, 3, 10, 4]
min_odd = None

for num in arr:
    if num % 2 != 0:
        if min_odd is None or num < min_odd:
            min_odd = num

if min_odd is not None:
    print("Smallest odd element:", min_odd)
else:
    print("No odd element found")