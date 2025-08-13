---
title: Classvariable
date: 2025-08-13
author: Your Name
cell_count: 2
score: 0
---

```python
class Classvariablepg:
    family = "families"
    def __init__(self, name,age):
        self.name = name
        self.age = age
print(Classvariablepg.family)

obj1  = Classvariablepg("Lavan",4)
obj2  = Classvariablepg("Gagan",5)
print(obj1.family)
print(obj2.family)

Classvariablepg.family = "relativies"
print(obj1.family)
print(obj2.family)  
```

    families
    families
    families
    relativies
    relativies



```python

```


---
**Score: 0**