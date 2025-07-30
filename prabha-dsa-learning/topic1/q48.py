# Read the smallest number from the even numbers.
arr = [5, 9, 2, 14, 8, 6, 13, 3, 10, 4]
min_even = None

for num in arr:
    if num % 2 == 0:
        if min_even is None or num < min_even:
            min_even = num
if min is not None:
    print("Smallest even element is:", min_even)
else:
    print("No even element found")





