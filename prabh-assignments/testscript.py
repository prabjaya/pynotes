from arithmetic import Arithmetic
from logical import Logical
from dunderrep import Dunderrep

if __name__ == '__main__':
    value1 = Arithmetic(10)
    value2 = Arithmetic(10)
    print(f"Arithmetic operation")
    print(f"First number:",value1)
    print(f"secondnumber:",value2)
    print(f"Addition(+): {value1.__add__(value2)}") 
    print(f"Subtration(-):{value1.__sub__(value2)}")
    print(f"Multiplication(*):{value1.__mul__(value2)}")
    print(f"Division(/): {value1.__truediv__(value2)}")
    value1 = Logical(100)
    value2 = Logical(200)
    print("\n")
    print("Logical Operation")
    print(f"First number:",value1)
    print(f"second number:",value2)
    print(f"Less than (<): {value1.__lt__(value2)}")
    print(f"Less than or equal to (<=): {value1.__le__(value2)}")
    print(f"Equal to (==): {value1.__eq__(value2)}")
    print(f"Not equal to (!=): {value1.__ne__(value2)}")
    print(f"Greater than (>): {value1.__gt__(value2)}")
    print(f"Greater than or equal to (>=): {value1.__gt__(value2)}")
    print("\n")
    print("Dunderp")
    obj1 = Dunderrep(10,10)
    print(repr(obj1))



