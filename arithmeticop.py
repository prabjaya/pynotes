class Arithmeticop:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def disply(self):
        print(f"value1 : {self.value1}, value2: {self.value2}")

    def add(self):
        return self.value1 + self.value2

    def sub(self):
        return self.value1 - self.value2

    def mul(self):
        return self.value1 * self.value2

    def div(self):
        return self.value1 / self.value2
    
obj1 = Arithmeticop(10,10)
obj1.disply()
print("Arithmetic operation")
print("Addition(+):", obj1.add())
print("Subtraction(-):",obj1.sub())
print("Multiplication(*):",obj1.mul())
print("Division(/):",obj1.div())












    
    