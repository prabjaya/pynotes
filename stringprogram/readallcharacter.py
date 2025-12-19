def readallcharacters(s):
    for i in range(len(s)):
        print(s[i]) 

readallcharacters("Hello")


def readcharacter(s):
    result = []
    for i in range(len(s)):
        print(s[i])
        result.append(s[i])
    return result


result = readcharacter("Kala")
assert len(result) == 4
print("All tests passed.")

print("While loop")

s = "Python"
i = 0
while i < len(s):
    print(s[i])
    i +=1 