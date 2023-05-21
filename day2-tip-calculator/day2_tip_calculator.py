#09-07-2021
print("Welcome to the tip Calculator! ")
bill = float(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like to give? 10%, 15% or 20%? "))
number_of_people = int(input("How many people to split the bill? "))
overall = (bill*(tip_percent*0.01))+bill
print("Each person should pay "+str(overall/2))
