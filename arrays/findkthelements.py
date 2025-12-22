def findkthelements(n,arr,k):
    arr.sort()
    print(arr)
    return arr[-k]
print("Kth largest element in the array is:")
print(findkthelements(7,[1,3,5,7,9,2,4],1))

print("kth smallest element in the array is:")
def findkthsmallestelements(n,arr,k):
    arr.sort()
    print(arr)
    return arr[k-1]

print(findkthsmallestelements(7,[1,3,5,7,9,2,4],3))



