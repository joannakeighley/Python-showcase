import math

# explain the choices to the user
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("")
print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond         - to calculate the amount you'll have to pay on a home loan")
print("")

# user inputs choice
selection = input("Investment or Bond: ")

option_1 = 'investment'
option_2 = 'bond'

# if 'investment' is selected
if selection.lower() == option_1.lower():
    deposit = float(input("Amount depositing: "))
    interest_rate = float(input("Interest rate: "))
    years = int(input("Number of years to invest: "))
    interest = input("'Simple' or 'Compound' interest? ")

# SIMPLE or COMPOUND
    option_a = 'simple'
    option_b = 'compound'

# if simple
    if interest.lower() == option_a.lower():
        total_amount = deposit*(1+(interest_rate/100)*years)
        print(f"The amount after {years} years is £{round(total_amount, 2)}")
# if compound
    elif interest.lower() == option_b.lower():
        total_amount = deposit*math.pow((1+(interest_rate/100)),years)
        print(f"The amount after {years} years is £{round(total_amount, 2)}")
    else:
        print("Invalid type of interest selected.")

# if 'bond' is selected
elif selection.lower() == option_2.lower():
    value = float(input("Present value of your house: "))
    interest_rate = float(input("Interest rate: "))
    months = int(input("Number of months to repay: "))
    monthly_interest = (interest_rate/100)/12

# amount to repay per month
    repay_amount = ((monthly_interest)*value)/(1-(1+(monthly_interest))**(-months))
    print(f"The repayment per month is £{round(repay_amount, 2)}")

# if input is invalid
else:
    print("An error has occurred.")
    print("Please choose either 'investment' or 'bond'.")