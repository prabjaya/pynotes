arr = [10, 20, 30, 40, 50, 60]
start = 0
end = len(arr) - 1

print("Output:", end=" ")
while start <= end:
    if start == end:
        print(arr[start], end=" ")
    else:
        print(arr[start], end=" ")
        print(arr[end], end=" ")
    start += 1
    end -= 1