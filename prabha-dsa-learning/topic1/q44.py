# Read the Elements from Both Ends of an Array, Starting from the Middle  
arr = [10, 20, 30, 40, 50, 60]
n = len(arr)

print("Output:", end=" ")
if n % 2 == 0:
    left = n // 2 - 1
    right = n // 2

    while left >= 0 and right < n:
        print(arr[left], end=" ")
        print(arr[right], end=" ")
        left -= 1
        right += 1
else:
    center = n // 2
    print(arr[center], end=" ")
    offset = 1

    while center - offset >= 0 or center + offset < n:
        if center - offset >= 0:
            print(arr[center - offset], end=" ")
        if center + offset < n:
            print(arr[center + offset], end=" ")
        offset += 1
