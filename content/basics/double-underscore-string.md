---
title: Double-Underscore-String
date: 2025-08-13
author: Your Name
cell_count: 3
score: 0
---

```python
#  created at : 20250118
```


```python
class Dusp:
    def __init__(self,name,age):
        self.name  = name
        self.age = age

    def __str__(self):
        return f"Person(Name = {self.name}, age = {self.age})"
obj = Dusp('Lavan',4)
print(obj)

    
```

    Person(Name = Lavan, age = 4)



```python

```


---
**Score: 0**