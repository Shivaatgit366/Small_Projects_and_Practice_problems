# Take two numbers a and b as the input, then generate a random number between a and b.
# The aim of the game is to guess the generated number with less number of attempts.
# 2 players are playing the game. Take inputs from the players till they give correct guess. Declare the winner.
# In each attempt, give commentary whether the input number needs to be >/ smaller than the previous input number.

# solution :-
# import random

# def guess_secret_number_player1(x, y, secret):  # a function is written which handles number guessing work.
#     guess_p1 = int(input("Guess the number in the range [a, b]\n"))
#     number_of_guesses_p1 = 1  # not to get the error, we can initialize the variable and set to none.
#     while guess_p1 != secret_number_player1:
#         if guess_p1 > secret_number_player1:
#             guess_p1 = int(input("Please enter the smaller number\n"))
#             number_of_guesses_p1 = number_of_guesses_p1 + 1  # for every condition, we should give increment statement.
#         elif guess_p1 < secret_number_player1:
#             guess_p1 = int(input("Please enter the bigger number\n"))
#             number_of_guesses_p1 = number_of_guesses_p1 + 1  # for every condition, we should give increment statement.
#     print(f"You have guessed the number in {number_of_guesses_p1} attempts")
# Remember :- Above print statement can not be written after the return statement.
# It is because function definition is not completed. We can only write print() outside the function definition.
#     return number_of_guesses_p1


# def guess_secret_number_player2(x2, y2, secret2):  # a function is written which handles number guessing work.
#     guess_p2 = int(input("Guess the number in the range [a, b]\n"))
#     number_of_guesses_p2 = 1  # not to get the error, we can initialize the variable and set to none.
#     while guess_p2 != secret_number_player2:
#         if guess_p2 > secret_number_player2:
#             guess_p2 = int(input("Please enter the smaller number\n"))
#             number_of_guesses_p2 = number_of_guesses_p2 + 1  # for every condition, we should give increment statement.
#         elif guess_p2 < secret_number_player2:
#             guess_p2 = int(input("Please enter the bigger number\n"))
#             number_of_guesses_p2 = number_of_guesses_p2 + 1  # for every condition, we should give increment statement.
#     print(f"You have guessed the number in {number_of_guesses_p2} attempts")
# Remember :- Above print statement can not be written after the return statement.
# It is because function definition is not completed. We can only write print() outside the function definition.
#     return number_of_guesses_p2


# if __name__ == '__main__':
#     a = int(input("Enter the first number a\n"))
#     b = int(input("Enter the second number b\n"))
#     secret_number_player1 = random.randint(a, b)  # this generates integer in the range [a, b]
#     secret_number_player2 = random.randint(a, b)  # we created two variables for 2 players.

    # print("Player 1 should start the game, Plz guess the number")
    # p1 = guess_secret_number_player1(a, b, secret_number_player1)

    # print("Player 2 should start the game, Plz guess the number")
    # p2 = guess_secret_number_player2(a, b, secret_number_player2)

    # if p1 < p2:
    #     print("Player 1 wins the game")  # number of guesses should be less for winning the game.
    # elif p1 > p2:
    #     print("Player 2 wins the game")  # number of guesses should be less for winning the game.
    # else:
    #     print("The game is tied")

    # print(f"Secret number for Player 1 was {secret_number_player1}")
    # print(f"Secret number for Player 2 was {secret_number_player2}")

# -----------------------------*-----------------------------*-----------------------------------*------------------
# -----------------------------*-----------------------------*-----------------------------------*------------------

# Another method from the youtube:-
# Concept:- Do not change anything in the function as we have seen in previous example.
# Only variables and the input parameters will be changed, function will not be touched.

import random


def guess_number(x, y, actual):
    guesswork = int(input(f"Guess the number in the range [{x}, {y}]\n"))
    nguess = 1
    while guesswork != actual:
        if guesswork < actual:
            guesswork = int(input("Plz enter the bigger number\n"))  # "guesswork" variable needs input value.
            nguess = nguess + 1
        else:
            guesswork = int(input("Plz enter the smaller number\n"))  # "guesswork" variable needs input value.
            nguess = nguess + 1
    print(f"You have guessed the number in {nguess} attempts")
    return nguess


if __name__ == '__main__':

    a = int(input("Enter the number a\n"))
    b = int(input("Enter the number b\n"))


    actual_number_p1 = random.randint(a, b)
    actual_number_p2 = random.randint(a, b)

    print("Player 1 starts the game, plz guess the number")
    player1_nguess = guess_number(a, b, actual_number_p1)  # we get only number of guesses done by the player.

    print("Player 2 starts the game, plz guess the number")
    player2_nguess = guess_number(a, b, actual_number_p2)  # we get only number of guesses done by the player.

    if player1_nguess < player2_nguess:
        print(f"Player 1 wins the game, Player 1 takes {player1_nguess} attempts")
    elif player1_nguess > player2_nguess:
        print(f"Player 2 wins the game, Player 2 takes {player2_nguess} attempts")
    else:
        print("Game is tied")

    print(f"Secret number for the Player 1 was {actual_number_p1} and attempts done is {player1_nguess}")
    print(f"Secret number for the Player 2 was {actual_number_p2} and attempts done is {player2_nguess}")

# -----------------------------*-----------------------------*-----------------------------------*------------------
# -----------------------------*-----------------------------*-----------------------------------*------------------
