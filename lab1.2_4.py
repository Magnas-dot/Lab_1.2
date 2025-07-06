#4. Write a program to print the multiplication table of a given number using a for loop.
num=int(input("Enter a positive number"))
for i in range(1,11):
    product=i*num

    print(f"{num} x {i} ={product}")
