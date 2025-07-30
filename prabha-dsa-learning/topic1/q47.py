# Finding Biggest even number in the given list
arr = [5, 9, 2, 14, 8, 6, 13, 3, 10, 4]
max_even = None

for num in arr:
    if num % 2 == 0:
        if max_even is None or num > max_even:
            max_even = num

if max_even is not None:
    print("Biggest even element:", max_even)
else:
    print("No even element found")