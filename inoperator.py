num = [10,20,30,40,12,1,90]
print(10 in num)
print(35 in num)
print(90 in num)


# for
for i in 'Python keyword':
    print(i)

# range
for count in range(1,5):
    print("Scientech Easy, Dhanbad")


# while
count = 0 
while(count < 3):
    print("Current count is",count)
    count = count + 1
print("While loop end")

#break
for i in range(1,7):
    if(i == 6):
        break
    print(i)
     


print("continue")
for i in range(1,7):
    if(i == 5):
        continue
    print(i)