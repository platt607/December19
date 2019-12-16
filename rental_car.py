import sys
'''
Section 1: Collect customer input
'''

##Collect Customer Data - Part 1

##1)	Request Rental code:
#Prompt --> "(B)udget, (D)aily, or (W)eekly rental?"
#rentalCode = ?
#get input as a string from customer and set equal to rentalCode
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
#2)	Request time period the car was rented.

#Prompt --> "Number of Days Rented:"
#rentalPeriod = ?
#	OR
#Prompt --> "Number of Weeks Rented:"
#rentalPeriod = ?
#if elif else branch statement that sets rentalPeriod equal to correct input and if no input exits the program
if rentalCode=='D':
  rentalPeriod = float(input("Number of Days Rented:\n"))
elif rentalCode=='B':
  rentalPeriod = float(input("Number of Days Rented:\n"))
elif rentalCode=='W':
  rentalPeriod = float(input("Number of Weeks Rented:\n"))
else:
  print('please check if input is correct')
  exit()


#Calculation Part 1

##Set the base charge for the rental type as the variable baseCharge. 
#The base charge is the rental period * the appropriate rate:
#declare variables and set equal to constant amount that is float therfore variable is typed as float
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00
#set appropriate baseCharge based on user input
#branch if elif statement that calculated baseCharge correctly based on user input rentalCode
if rentalCode == 'B':
  baseCharge = float(rentalPeriod) * budgetCharge
elif rentalCode == 'D':
  baseCharge = float(rentalPeriod) * dailyCharge
elif rentalCode == 'W':
  baseCharge = float(rentalPeriod) * weeklyCharge

#Collect Customer Data - Part 2

#4)Collect Mileage information:
#a)	Prompt the user to input the starting odometer reading and store it as the variable odoStart

#Prompt -->"Starting Odometer Reading:\n"
# odoStart = ?
# set starting odometer reading a numeric value input parameter equal to odoStart and changing it to an integer type variable
odoStart = int(input("Starting Odometer Reading:\n"))

#b)	Prompt the user to input the ending odometer reading and store it as the variable odoEnd

#Prompt -->"Ending Odometer Reading:"
# odoEnd = ?
#  set ending odometer reading a numeric value input parameter equal to odoEnd and changing it to an integer type variable
odoEnd = int(input("Ending Odometer Reading:\n"))
#c) Calculate total miles
totalMiles = abs(odoEnd - odoStart)



# Calculate Charges 2

##	Calculate the mileage charge and store it as 
#   the variable mileCharge:

#a)	Code 'B' (budget) mileage charge: $0.25 for each mile driven
#branch statement if elif with nested if elif that calculates rental charges based on inputs
if rentalCode=='B':
  mileCharge = totalMiles * 0.25
#b)	Code 'D' (daily) mileage charge: no charge if the average
#   number of miles driven per day is 100 miles or less;
#   i)	Calculate the averageDayMiles (totalMiles/rentalPeriod)

#   ii)	If averageDayMiles is above the 100 mile per day
#       limit:
#     (1)	calculate extraMiles (averageDayMiles  - 100)
#     (2)	mileCharge is the charge for extraMiles, 
#         $0.25 for each mile
elif rentalCode == 'D':
  averageDayMiles = totalMiles / int(rentalPeriod)#change rentalPeriod variable from string to integer type
  if averageDayMiles <= 100:
    mileCharge = 0
  elif averageDayMiles > 100:
    mileCharge = (averageDayMiles - 100) * 0.25


#c)	Code 'W' (weekly) mileage charge: no charge if the 
#   average number of miles driven per week is 
#   900 miles or less;
 
#   i)	Calculate the averageWeekMiles (totalMiles/ rentalPeriod)

#   ii)	mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles
elif rentalCode == 'W':
  averageWeekMiles = totalMiles / int(rentalPeriod)#change rentalPeriod variable from string to integer type
  if averageWeekMiles <= 900:
    mileCharge = 0.00
  elif averageWeekMiles > 900:
    mileCharge = 100.00 * int(rentalPeriod)#change rentalPeriod variable from string to integer type   
#calculate amount due for rental
amtDue = baseCharge + mileCharge
#print rental summary and format appropriately 
print('Rental Summary')
print('Rental Code:       {}'.format(rentalCode))
print('Rental Period:     {0:g}'.format(rentalPeriod))
print('Starting Odometer: {}'.format(odoStart))
print('Ending Odometer:   {}'.format(odoEnd))
print('Miles Driven:      {}'.format(totalMiles))
print('Amount Due:        ${:,.2f}'.format(amtDue))#format as money and as float with two decimals