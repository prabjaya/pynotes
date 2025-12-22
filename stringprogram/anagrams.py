from collections import Counter

def anagrams(a:str,b:str)->bool:
    return Counter(a) == Counter(b)



print(anagrams("cat","act"))
