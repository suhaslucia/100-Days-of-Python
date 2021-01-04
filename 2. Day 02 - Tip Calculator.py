print(" ----- Tip Calculator ----- ")

# Taking the inputs as a float value from the user
bill = float(input("What is the total bill?  "))
percentage = float(input("What percent of tip would you like to give?  "))
total_person = float(input("How many people to split the bill?  "))

# Calculating the Values
tip = percentage / 100 * bill           # Calculating the tip amount
total_bill = tip + bill                 # Calculating the total bill
split_bill = total_bill / total_person # Calculating the split bill

print(split_bill) # Printing the split amount for each person
