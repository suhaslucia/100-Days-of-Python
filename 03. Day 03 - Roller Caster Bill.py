# Printing the heading
print(" ----- Roller Caster Game ----- ")

# Taking the height in centimeters as a integer value from the user and creating variable 'bill' for future calculations
height = int(input("Enter your height in cm: "))
bill = 0

# Checking the height value if its greater than 180cms or not
if height >= 180:
    print("Congrats, You are eligible to play a game. ")

    # Taking the age as a integer value from the user
    age = int(input("Enter your age to continue: "))
    if age <= 12:
        bill = 5  # Tickets price is $5 for children.
        print("Children's ticket price is $5.")
    elif age <= 18:
        bill = 7  # Tickets price is $7 for youth.
        print("Youth's ticket price is $7. ")
    elif 45 <= age <= 55:
        bill += 0   # Tickets price is $0 for mid age.
        print("Free ticket for this age. ")
    else:
        bill = 12   # Tickets price is $12 for adults.
        print("Adult's ticket price is $12. ")

    # Asking the user for if they want photo or not
    photo = input("Do you want photos ? type 'Y' or 'N': ")
    if photo == 'Y':
        print("Addition of $3 will be added.")
        bill += 3  # Additional of $3 will be added to the bill
    print(f"Your total bill is ${bill}")

else:
    print("Sorry, You are too short for the game. ")
