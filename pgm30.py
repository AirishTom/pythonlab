list=[1,45,8,3,4,77,100,2,6]
print("list",list)
even=[]
odd=[]
for num in list:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("list removing even=",odd)


