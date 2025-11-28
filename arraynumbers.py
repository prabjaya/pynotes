def arrynumber(num):
    return [i for i in range(num)]

print(arrynumber(5))


result = arrynumber(10)
assert len(result) == 10
print(result)


result = arrynumber(20)
assert len(result) == 20
print(result)


print(type(arrynumber(3)))