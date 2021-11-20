# Rohan, a fraud wrote a python function to print a multiplication table of a given number with one value wrong.
# He did this to cheat classmates.
# So we ourselves wrote a Python program which corrects his multiplication table and points out his mistake.
# We expose him as a fraud.

# Rohan Das’s Function Input:
# rohanMultiplication(6)

# Rohan’s function returns this output:
# [6, 12, 18, 26,..., 60]

# ---------------------------*---------------------------*------------------------------*---------------------------
# Solution:-

# table_of = input("Multiplication table required for\n")
# multiplied_by = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# def fake_multiplication_table():
#     for x in table_of:
#         for y in multiplied_by:
#             if int(x) == y:
#                 print(26)
#             else:
#                 print(int(x) * y)

# fake_multiplication_table()

# def correct_multiplication_table():
#     for x in table_of:
#         for y in multiplied_by:
#             if int(x) == y:
#                 print("Rohan Das is a fraud,", end="")
#                 print(" correct value is, ", end="")
#                 print(int(x) * y)
#             else:
#                 print(int(x) * y)

# correct_multiplication_table()

# ----------------------*-------------------------*--------------------------*----------------------------*----------
# ----------------------*-------------------------*--------------------------*----------------------------*----------

# Solution from youtube:-

import random  # this module is imported to generate a random integer

def rohanmultiplication(num):  # a function which gives table. Number is the input value.
    wrong_index = random.randint(0, 9)  # an integer in the range [0, 9] will be formed.
    table = [num*i for i in range(1, 11)]  # I had taken a list of indices which had items from 1 to 20.
    # a correct table is formed, now we change any item in the table list.
    table[wrong_index] = table[wrong_index] + random.randint(1, 12)  # we get some wrong random number by this step.
    return table  # we get the list of items

def correct_table(anytable, anynumber):  # taken two arguments table and number
    for i in range(1, 11):
        if anytable[i - 1] != i * anynumber:  # if the table value doesn't match with (index * number), condition check.
            return (f"item {i} in the list is wrong")
    return None  # This function returns nothing, if the condition exists then only it returns some value.
# The above statement "return None" is not required at all.
# Function gives none automatically if the condition is not satisfied.


if __name__ == '__main__':

    n = int(input("Plz enter the number\n"))
    rohan_table = rohanmultiplication(n)
    print(rohan_table)
    print(correct_table(rohan_table, n))

# -----------------------*--------------------------*-------------------------*------------------------*----------
