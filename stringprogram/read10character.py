str = "abc de fghij klmno pqrst uvwxyz"
i = 0
while i < 10:
    if str[i] != ' ' :
        print(str[i])
    i = i + 1


print("Last 10 characters")
str = "hello test abc def ghij"
lenth = len(str)
i = lenth - 12
while i < lenth:
    if str[i] !=' ':
        print(str[i])
    i = i + 1   


print("last 10 characters with for loop")
str = "hello test abc def ghij"
lenthfor = len(str)

for i in range(lenthfor - 12,lenthfor):
    if str[i] != ' ':
        print(str[i])



print("Last 10 characters from right side")
str = "hello test abc def ghij"
print(str)
n = len(str)
i = n - 1
for count in range(10):
    print(str[i])
    i = i - 1


print("second way")
str = "hello test abc def ghij"
n = len(str)
for i in range(n-1,n-11,-1):
    print(str[i])