# A list with the numbers is given. We should print the list with next palindromic numbers in it.
# Condition is print the next palindromic number only if the number is > 10.
# Otherwise, keep the same number in the list.


# solution :-
# no_of_trials = int(input("Enter the number of items you will enter for the list\n"))
# user_list = [int(input("Enter the number one by one\n")) for x in range(no_of_trials)]
# print(f"Thank you, your list is {user_list}")

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# def next_palindromic_number(m):
#     if m > 10:
#         m = m + 1
#         while not is_palindrome(m):
#             m += 1
#         return m
#     else:
#         return m

# if __name__ == '__main__':
#     final_list = [next_palindromic_number(user_list[item]) for item in range(len(user_list))]
#     print(f"your required list is {final_list}")

# --------------------------*----------------------*----------------------*--------------------------*-------------
# --------------------------*----------------------*----------------------*--------------------------*-------------

# Solution from the Youtube:-
# here, 2 functions are not touched, they are kept same.
# Concept:- In this example, the required conditions are put inside the loop. Functions are untouched.

def is_palindrome(n):
    return str(n) == str(n)[::-1]
def next_palindromic_number(m):
        m = m + 1
        while not is_palindrome(m):
            m += 1
        return m

if __name__ == '__main__':
    no_of_trials = int(input("Enter the number of items you will enter for the list\n"))
    user_list = [int(input("Enter the number one by one\n")) for x in range(no_of_trials)]
    print(f"Thank you, your list is {user_list}")

    # new_output_list = []
    # for i in user_list:
    #     if i > 10:
    #         n = next_palindromic_number(i)
    #         new_output_list.append(n)
    #     else:
    #         i = i
    #         new_output_list.append(i)

    # print(f"your required list is {new_output_list}")


    # Using list comprehension we can write in one line:-
    # new_output_list =\
    #     [next_palindromic_number(user_list[i]) if user_list[i] > 10 else user_list[i] for i in range(len(user_list))]
    # print(f"your required list is {new_output_list}")
                                            # {or}
    # Using list comprehension we can write in one line:-
    # new_output_list =\
    #     [(user_list[i]) if user_list[i] <= 10 else next_palindromic_number(user_list[i]) for i in range(len(user_list))]
    # print(f"your required list is {new_output_list}")

# ---------------------*--------------------*-----------------------*--------------------------*--------------------
# ---------------------*--------------------*-----------------------*--------------------------*--------------------

