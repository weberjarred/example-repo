
# input user's age and store it as an integer variable called age
age = int(input("Enter your age: "))

if age > 100:   # if the user's age is greater than 100
    print("Sorry, you are dead.")
elif age >= 40:    # if the user's age is greater than or equal to 40
    print("You're over the hill.")
elif age >= 65:   # if the user's age is greater than or equal to 65
    print("Enjoy your retirement!")
elif age < 13:  # if the user's age is less than 13
    print("You qualify for the kiddie discount.")
elif age == 21: # if the user's age is equal to 21
    print("Congrats on your 21st!")
else:   # if the user's age is none of the above
    print("Age is but a number.")
