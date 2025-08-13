class Dunderrep:
    def __init__(self,value1,value2):
        self.value1  = value1
        self.value2 =  value2

    def __repr__(self):
        return f"('{self.value1}','{self.value2}')"

obj1 = Dunderrep(10,10)
print("__repr__:",obj1)
