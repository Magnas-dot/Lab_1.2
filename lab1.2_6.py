#6. Write a program that accepts 10 integers from the user and counts how many are positive, negative, and zero.

count_positive=0
count_negative=0
count_zero=0
for i in range (10):
    x=int(input("Enter Number: "))
    if(x>0):
        count_positive+=1
    elif(x<0):
        count_negative+=1
    else:
        count_zero+=1
print("Number of positive numbers:",count_positive)
print("Number of negative numbers:",count_negative)
print("Number of zero numbers:",count_zero)
