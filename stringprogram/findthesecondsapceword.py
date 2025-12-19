str ="hello test abc def ghij"

firstwordspace = str.find(' ')
secondwordspace = str.find(' ',firstwordspace + 1)

for i in range(firstwordspace + 1, secondwordspace):
    print(str[i])


print("while loop way")
fs = str.find(' ')
sp = str.find(' ', fs + 1)

while (fs + 1) < sp:
    print(str[fs + 1])
    fs = fs + 1
    