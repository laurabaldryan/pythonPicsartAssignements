#A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6, and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7,14, 28, and 28=1+2+4+7+14. However,15 is not a perfect number because its divisors are 1, 3, 5, 15, and 15 != 1 + 3 + 5. Write a program that finds all four of the perfect numbers that are less than 10000.

divisorsList=[1]
for number in range(1,10000):
    perfectNumbers=[]
    divisorsSum=0
    for i in range (1,number):
        if number%i==0:
            divisorsList.append(i)
            divisorsSum+=i
    if number==divisorsSum:
        perfectNumbers.append(number)
        print(perfectNumbers)



