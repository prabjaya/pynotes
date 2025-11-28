def partialwordcount(stringwards,partialword):
    count = 0
    for i in stringwards:
        if i.startswith(partialword):
            count +=1
    return count

stringwords=["car","cat","apple","man","carret"]
partialword = 'm'

print(partialwordcount(stringwords,partialword))



def partialwordcount(stringwards,partialword):

    return sum(1 for i in stringwards if i.startswith(partialword))

stringwords=["car","cat","apple","man","carret","carmodel"]
partialword = 'c'
lowercon = partialword.lower()
print(lowercon)

print(partialwordcount(stringwords,partialword))
