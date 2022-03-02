def longest(a):
    max1=len(a[0])
    temp=max1
    for i in a:
        if (len(i) > max1):
            max1 = len(i)
            temp = i
    print("The word with the largest length is:",temp,"and length is",max1)
a=['apple','pineapple','strawberry']
longest(a)