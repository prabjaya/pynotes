str = "hello test abc def ghij klmno pqrst uvwxyz"

i = 12
print(str)
while i >= 3:
    if str[i] != ' ':
        print(str[i])
    i = i - 1

print("Secondway for loop")
for i in range(12,2,-1):
    if str[i] != ' ':
        print(str[i])

for i in reversed(str[3:13]):
    if i != ' ':
        print(i)

