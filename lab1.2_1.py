#1. Write a program to check whether a given number is prime or not.

num=int(input("Enter a Positive Number:"))
count=0
for i in range(1,num+1):
        if(num%i==0):
            count+=1
if(count==2):
    print("given number is prime")
else:
    print("number is composite")
