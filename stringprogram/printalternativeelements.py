str = "abcdefghijklmn"
print("Alternative elements in the string:")
print(str)
for i in range(0,len(str),2):
    print(str[i])


print("Alternative elements in reverse order:")
for i in range(len(str)-1,-1,-2):
    print(str[i])
