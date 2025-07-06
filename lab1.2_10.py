#10.Write a menu-driven program to perform arithmetic operations (+, -, *, /) based on user choice using conditional statements.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
x=input("enter the operation you want to perform(+,-,/,*):")
match x:
   case '+':
    print("sum is:",a+b)
   case '-':
      print("difference is:",a-b)
   case '*':
      print("multiplication is:",a*b)
   case '/':
      print("division is:",a/b)
