#5. Write a program to find the largest and smallest number in a list entered by the user.
list_1=[]
n=int(input("How many numbers you want to enter? "))
for i in range(0,n):
    x=int(input("Enter Number: "))
    list_1.append(x)

list_1.sort()
print("Largest Number:",list_1[n-1])
print("smallest Number:",list_1[0])
