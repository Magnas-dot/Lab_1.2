#8. Write a program that reads a number and prints whether it is a palindrome or not.

num=int(input("Enter a Number:"))
temp=num
s=0
while num>0:
    r=num%10
    s=s*10+r
    num=num//10
if(s==temp):
    print("Entered number is palindrome")
else:
    print("Entered number is not palindrome")
