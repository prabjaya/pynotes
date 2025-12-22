str ="hello test abc def ghij"

i = str.rfind(' ') + 1
j = len(str) - 1


for k in range(i, j + 1):
    print(str[k])
