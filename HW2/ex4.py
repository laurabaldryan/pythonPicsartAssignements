#A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.

year=int(input("Eter the year : " ))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("The %d year is leap"%(year))
else:
    print("The year isn't leap" )

countnumbers= (year-1600)//4
print("The number of leap years between 1600 and %d is %d "%(year,countnumbers))
