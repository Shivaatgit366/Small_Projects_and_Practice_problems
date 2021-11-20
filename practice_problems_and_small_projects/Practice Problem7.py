# Searching the given phrase/keywords from the list of sentences and bring those sentences which has matches.
# Keyword matched sentences should be given as output with decreasing order of relevancy.
# Output should be those matched sentences with every letter in small case.


# solution:-
# Take 2 sentences as parameters. Get the value of "number of matches", we call it as "nmatch" in this example.
# def matchingwords(sentence1, sentence2):
#     words1 = sentence1.strip().split(" ")
#     words2 = sentence2.strip().split(" ")
#     nmatch = 0  # means number of matches is initialized to zero.
#     for x in words1:
#         for y in words2:  # this is the new concept simply means Combination iteration.
#             if x.lower() == y.lower():  # this condition is inserted inside.
#                 nmatch = nmatch + 1  # increment statement applied for nmatch.
#     return nmatch


# looping inside looping, this technique is very useful for combining the items between variables.
# Also this technique helps us to get more iterations.

# if __name__ == '__main__':

    # print(matchingwords("This is good", "python is good"))  # testing the function
    # (This, python), (This, is), (This, good), (is, python), (is, is), (is, good)
    # (good, python), (good, is), (good, good)
    # out of 15, only 9 combination we get, use it with f string to print and see the iteration results.

    # sentences = ["Python is a good", "This is a snake",
    #              "Harry is a good boy", "Subscribe to my channel"]

    # query = input("Please enter the query string\n")

    # list_of_nmatches = [matchingwords(query, i) for i in sentences]  # list with number of matches per each sentence.

    # convert it to zip
    # zip_of_nmatchlist_sentenceslist = zip(list_of_nmatches, sentences)

    # Remember:- Item of a zipped file will be in tuple format like this  (list1 item, list2 item)
    # we get the location of the zipped object if we print just the variable.

    # when we use sorted function, we get output in list format.
    # We get list with each item as a tuple.

    # sorted_decreasingly = sorted(zip_of_nmatchlist_sentenceslist, reverse=True)  # it sorts in reverse direction.
    # it gives a list with zipped and sorted in decreasing order of matches.

    # Finally, we will make another final list taking all the items from the sorted list.
    # We will add few conditions to eliminate zero match items.

    # See, the below codes.
    # final_list = [m for m in sorted_decreasingly if (m[0] != 0)]  # list will be empty if condition doesn't exist.
    # Remember :- Here we can see clearly, "m" means a tuple with 2 items.

    # print(f"{len(final_list)} results found!")
    # Note: if we don't get any match in any sentences, "final list" will be empty.
    # If a list is empty, then len(list) is 0.

    # print(final_list)
    # for a, b in final_list:
    #     print(f"\"{b}\" was found with \"{a}\" match")

# ---------------------*---------------------*----------------------*--------------------------*--------------------
# ---------------------*---------------------*----------------------*--------------------------*--------------------

# Python String strip() Method:-  Syntax    string.strip(characters)
# See the below example, remove the front and back spaces in the string.
# Remove spaces at the beginning and at the end of the string:
# txt = "     banana     "
# x = txt.strip()  # strip() removes front and back spaces by default.
# print("of all fruits", x, "is my favorite")


# See another example where few characters are removed from the string.
# string1 = ",,,,,rrttgg.....banana....rrr"
# y = string1.strip(",.rtg")
# print(y)  # we get the result as    banana

# ----------------------------*-------------------------------*--------------------------------*----------------------
