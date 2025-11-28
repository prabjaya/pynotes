def partialwordcount(stringwards,partialword):
    count = 0
    for i in stringwards:
        if i.startswith(partialword):
            count +=1
    return count

stringwords=["car","cat","apple","man","carret","carmodel"]
partialword = 'm'

print(partialwordcount(stringwords,partialword))
