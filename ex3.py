#Write a program that asks the user to enter two numbers, x, and y, and computes | x − y | /  x+y.

x= float(input("Enter the x : "))
y= float(input("Enter the y : "))
result = (x-y)/(x+y)
if result>=0:
    print("The result of |x-y|/ x+y = " , result)
else: 
    #result *= -1 
    print("The result of |x-y|/ x+ y = " , -result) 
