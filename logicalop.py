class Logicalop:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def disply(self):
        print(f"value1 : {self.value1}, value2: {self.value2}")

    def lessop(self):
        return (self.value1 < self.value2)
   
    def lessequal(self):
        return (self.value1 <= self.value2)
    
    def greaterthan(self):
        return (self.value1 > self.value2)
    
    def greaterthanequal(self):
        return (self.value1 >= self.value2)

    def equal(self):
        return (self.value1 == self.value2)
    
    def notequal(self):
        return (self.value1 != self.value2)
    
obj1 = Logicalop(10,10)
obj1.disply()
print("Logical operation")
print("Less than or equal to (<=)",obj1.lessop())
print("Less than equal<=:",obj1.lessequal())
print("Greater than (>):",obj1.greaterthan())
print("Greater than or equal to (>=):",obj1.greaterthanequal())
print("Equal to (==):",obj1.equal())
print("Not equal to (!=):",obj1.notequal())













    
    