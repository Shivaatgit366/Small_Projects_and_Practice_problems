# Take age or year as an input from the user and tell them when they turn 100 year old.
# Also handle many types of errors which comes during the execution.

# solution:-
# current_year = 2021
# print("welcome to the age calculator game")
# user_age = str(int(input("Enter the year of birth or Enter your age\n")))

# def ageadditor():
#     if len(user_age) == 2:  # put double equal symbol.
#         return (current_year + (100 - int(user_age)))  # here user_age variable is a string, convert to int.
#     elif len(user_age) == 4:
#         return (current_year + (100 - (current_year - int(user_age))))

# calculated_year = ageadditor()

# if __name__ == '__main__':
#     print(f"when you become 100 years old, the year will be {calculated_year}")

# --------------------------*-------------------------*---------------------------*-----------------------*---------

# Another solution from the youtube:-
# this is modified by me in the end.


# current_year = 2021
# yearAge = int(input("What is your age/ year of birth?\n"))
# isAge = False  # a variable is assigned with a boolean value False.
# isYear = False  # same technique as used above.


# if len(str(yearAge)) == 4:
#     isYear = True  # the variable is true only if the condition is satisfied.
# if len(str(yearAge)) == 1 or 2:
#     isAge = True  # if the age is given as input, then isAge variable is true.

# if len(str(yearAge)) == 3:
#     print("you are too old to play this game")
#     exit()
# if (yearAge < 1900 and isYear):
#     print("you are the oldest person alive on the planet Earth")
#     exit()
# if (yearAge > 2021):
#     print("You are not yet born")
#     exit()

# if isAge:  # this means if the isAge is True, then the below condition exists.
#     balance_Age_forcentury = 100 - yearAge  # we get required difference to become hundred.
# if isYear:  # this means if the isYear is True, then the below condition exists.
#     balance_Age_forcentury = 100 - (current_year - yearAge)  # we get required difference to become hundred.

# print(f"You will be hundred years old in the year {current_year + int(balance_Age_forcentury)}")

# interestedYear = int(input("Enter the year you want to know your age in\n"))

# if isYear:
#     print(f"You will be {(current_year - yearAge) + (interestedYear - current_year)} years old in {interestedYear}")

# elif isAge:
#     print(f"You will be {yearAge + (interestedYear - current_year)} years old in {interestedYear}")

# ----------------------*----------------------*--------------------------*-------------------------*---------------

