 #9. Write a program that finds all numbers between 100 and 999 where the sum of the cubes of the digits equals the number itself (Armstrong numbers).
num=int(input("Enter a Number between 100 and 999:"))
temp=num
s=0
while num>0:
    r=num%10
    s=s+r*r*r
    num=num//10
if(s==temp):
    print("Entered number is Armstrong")
else:
    print("Entered number is not Armstrong")
