#3.Write a program that reads a number and prints the factorial of that number using a while loop.
num=int(input("Enter a number:"))
num_o=num
fact=1
while(num!= 1):
    fact=fact*num
    num-=1
print(f"factorial of {num_o} is {fact}")
