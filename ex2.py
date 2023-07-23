#Write a program that generates and prints 50 random integers, each between 3 and 6.
import random
print("50 random numbers generated between 3 and 6 ") 
for i in range(0,50):
    number= random.randint(3,6)
    print(number)
