class Arithmetic:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __add__(self,secondnumber):
        return Arithmetic(self.value + secondnumber.value)

    def __sub__(self,secondnumber):
        return Arithmetic(self.value - secondnumber.value)

    def __mul__(self,secondnumber):
        return Arithmetic(self.value * secondnumber.value)

    def __truediv__(self,secondnumber):
        return Arithmetic(self.value / secondnumber.value)
