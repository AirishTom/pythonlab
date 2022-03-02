#program to calculate student total and percentage
name=input("enter the student name")
print("enter the marks out of 100")
sub1=int(input("enter the mark in python"))
sub2=int(input("enter the mark in C"))
sub3=int(input("enter the mark in Java"))
sub4=int(input("enter the mark in C++"))
sub5=int(input("enter the mark in php"))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print("total marks scored",total)
print("total percentage is",percentage)
