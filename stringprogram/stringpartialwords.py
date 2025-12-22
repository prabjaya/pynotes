def stringpartialwords(stringwords,partialword):
    return [word for word in stringwords if word.startswith(partialword.lower())]

print(stringpartialwords(["Car","cat","apple","man","carret","carmodel"],'c'))
