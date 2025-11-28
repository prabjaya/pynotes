stringwords=["car","cat","apple","man"]
partialword = 'c'

result =[]
for i in stringwords:
    if i.startswith(partialword):
        result.append(i)

print(result)


def partialwordidentify(stringwards,partialword):
    res = []
    for i in stringwards:
        if i.startswith(partialword):
            res.append(i)

    return res

stringwords=["car","cat","apple","man","carret","carmodel"]
partialword = 'c'

print(partialwordidentify(stringwords,partialword))


resulttest = partialwordidentify(stringwords,partialword)
assert len(resulttest) == 4
