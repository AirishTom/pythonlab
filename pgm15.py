
op=(input("enter the operator"))
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if op=='+':
     print(num1+num2)
elif op=='-':
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif op=='*':
    print(num1*num2)
elif op =='/':
    print(num1/num2)
else:
    print("INVALID")
