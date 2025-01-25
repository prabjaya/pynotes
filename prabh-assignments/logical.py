class Logical:
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
       return str(self.value)

    def __lt__(self,secondnumber):
        return Logical(self.value < secondnumber.value)

    def __le__(self,secondnumber):
        return Logical(self.value <= secondnumber.value)

    def __eq__(self,secondnumber):
        return Logical(self.value == secondnumber.value)
    
    def __ne__(self,secondnumber):
        return Logical(self.value != secondnumber.value)

    def __gt__(self,secondnumber):
        return Logical(self.value > secondnumber.value)

    def __ge__(self,secondnumber):
        return Logical(self.value >= secondnumber.value)

