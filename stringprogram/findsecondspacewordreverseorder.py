str = "hello test abc def ghij"

fs = str.find(' ')
ss = str.find(' ',fs + 1)

for i in range(ss -1,fs,-1):
    print(str[i])

print("third space word in reverse order")
fs = str.find(' ')
ss = str.find(' ',fs + 1)
ts = str.find(' ',ss + 1)

for i in range(ts -1,ss,-1):
    print(str[i])