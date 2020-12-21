#TIP CALCULATOR

print("Welcome to tip calculator")

#TAKE INPUT 
bill = float(input("What was the total bill? "))
tip = float(input("What percent tip would you like to give ? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))

#CALCULATE
individual_amt = (bill*(1+tip/100))/people
print("Each person should pay: "+str(individual_amt))
