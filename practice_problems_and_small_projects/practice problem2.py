# Harry Potter has n apples. He is a teacher, and he wants to donate the apples to his students.
# Print the number in the range mn to mx is divisor of n or not.

# solution using both the loops:-

# print("Hi students! This is Harry, I want to distribute the apples to you")
# no_of_apples = int(input("Enter the total number of apples from which you want to distribute to the students\n"))
# first_no_of_range = int(input("Enter the first number of range\n"))
# second_no_of_range = int(input("Enter the second number of range\n"))

# for x in range(first_no_of_range, second_no_of_range+1):
#     if no_of_apples % x == 0:
#         print(f"{x} is a divisor of {no_of_apples}")
#     elif no_of_apples % x != 0:
#         print(f"{x} is not a divisor of {no_of_apples}")
    # x = x + 1  this increment statement is not required in for loop. If it is given, then no problem.

# if __name__ == '__main__':
#     if first_no_of_range == second_no_of_range:
#         print("you have entered the same number, sorry try again")
#         exit()

# -------------------------*-------------------------*-------------------------*-------------------------*------------

# print("Hi students! This is Harry, I want to distribute the apples to you")
# no_of_apples = int(input("Enter the total number of apples from which you want to distribute to the students\n"))
# first_no_of_range = int(input("Enter the first number of range\n"))
# second_no_of_range = int(input("Enter the second number of range\n"))

# x = first_no_of_range
# while x in range(first_no_of_range, second_no_of_range+1):  # DON'T put  < second_no_of_range + 1
#     if no_of_apples % x == 0:  # since x is already in the range, it takes care of the "less than" condition.
#         print(f"{x} is a divisor of {no_of_apples}")
#     elif no_of_apples % x != 0:
#         print(f"{x} is not a divisor of {no_of_apples}")
#     x = x + 1  # Do not forget to put the increment statement.

# if __name__ == '__main__':
#     if first_no_of_range == second_no_of_range:
#         print("you have entered the same number, sorry try again")
#         exit()
# ------------------------*------------------------*---------------------*------------------------*----------------

