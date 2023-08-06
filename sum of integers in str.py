Str = "PYTHON432AWS4569"
sum = 0
for i in Str:
    #check if values lies between range of numbers or not
    #according to ascii tale
    if ord(i) >= 48 and ord(i) <= 57:

        sum = sum + int(i)
print('Sum is :' + str(sum))