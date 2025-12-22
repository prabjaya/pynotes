str = "hello test abc def ghij"
fs = str.find(' ')

for i in range(fs - 1,-1,-1):
    print(str[i])
