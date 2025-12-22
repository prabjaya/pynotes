from collections import Counter


def first_unique(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_unique("awis"))

print("another way")

def find_unique(s):
    result = []
    for char in s:
        if s.count(char) == 1:
            result.append(char)
    return result
        
print(find_unique("swiss"))