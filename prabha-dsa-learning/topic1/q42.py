# Read first and second element sum is equal to next elemnts

arr = [1,2,3,5,8,13,21]

for i in range(len(arr)-2):
    if(arr[i] + arr[i+1] == arr[i+2]):
        print(i,end= " ")

