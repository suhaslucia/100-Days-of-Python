# Printing the Heading
print(" ----- Pizza Ordering ----- ")

# Taking the inputs from the user for size, topping, cheese of the pizza
size = input("Enter the Size of the pizza 'S', 'M', 'L': ")
topping = input("Do you want Pepperoni ? 'Y', 'N': ")
cheese = input("Do you want Cheese ? 'Y', 'N': ")
bill = 0

# Checking for the pizza size is small
if size == "S":
    bill += 15
    if topping == "Y":
        bill += 2
    if cheese == "Y":
        bill += 1
    print(f"Your total bill is {bill}")

# Checking for the pizza size is medium
if size == "M":
    bill += 20
    if topping == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
    print(f"Your total bill is {bill}")

# Checking for the pizza size is large
if size == "L":
    bill += 25
    if topping == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
    print(f"Your total bill is {bill}")
