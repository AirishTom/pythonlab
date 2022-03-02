current = int(input("enter the current year"))
final = int(input("enter the final year"))
for num in (range(current,final)):
    if num%4 == 0:
        print(num)