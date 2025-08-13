def func(): 
    i = 10
    if (i == 1):
        print("Hello world")
    elif(i == 10):
        print("Hi")
    else:
        print("Hi How are you")

func()


# Python Return Keywords – Return, and Yield
def funwithreturn():
    i = 20
    return i

def withoutreturn():
    i = 30

print(funwithreturn())
print(withoutreturn())

# Yeild:

def funyield():
    x = 0
    for i in range(5):
        x = x + i
        yield x
for i in funyield():
  print(i)

# with
with open("sample.txt",'w')as file:
    file.write('Learning Python Language')
print("successfully added")