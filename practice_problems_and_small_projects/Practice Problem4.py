# We should find the next palindrome from the user's input.
# First input should be number of trials in which user going to enter the numbers.
# Later, take all the input numbers given by the user. Then, give the next palindrome to the every number.


# solution:-
# using list comprehension technique, we can avoid creating empty list and append command. See below.
no_of_tests = int(input("Enter the number of tests you are going to conduct\n"))
user_input_list = [int(input("Enter the numbers you want to test, enter one by one\n")) for x in range(no_of_tests)]
print(f"Ok, your list is {user_input_list}")  # input list is prepared.

def is_palindromic(m):  # m is an integer and it can have any number of digits.
    return str(m) == str(m)[::-1]  # this return keyword gives the boolean value either True or False.
# Remember:- Just like "print" keyword, "return" keyword also gives the boolean value for conditional statement.
# This function will have either True or False value in it.

# Remember :- While loop does the iteration process until the given condition is True.
# we know, while i < 6 and i starts from 1, while loop does the iteration process till condition is true.

def next_palindrome(i):
    i = i + 1  # i value starts from (i + 1)
    while not is_palindromic(i):  # Note:- it is same as writing like this     while is_palindromic(i) == False:
        i += 1
    return i  # Meaning:- after completing the iteration process, function returns final value of i.

if __name__ == '__main__':
    for item in range(len(user_input_list)):
        print(f"Next Palindrome for {user_input_list[item]} is {next_palindrome(user_input_list[item])}")

# -------------------------*------------------------*------------------------*-----------------------*------------
