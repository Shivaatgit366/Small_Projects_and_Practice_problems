# Imagine we visited a restaurant. Food items are sorted based on calories. Take a list as an input.
# Make 4 techniques to reverse the list.
# 1) In built method 1
# 2) In built method 2
# 3) list slicing trick
# 4) Using for loop, swap first element to last one, second element to second last one and so on..

# Remember :- All the 4 methods will give the same results. They reverse the list items.
# operator "/" stands for division, operator "//" stands for floor division.

# reverse():-
# it reverses the contents of the list object in-place. It directly modifies the original list.

# reversed():-
# it doesn't reverse a list in-place(modify original list), it doesn't create any copy of the list.
# This function gets a reverse iterator which is used to cycle through the list. see the example below.
# def Reverse(lst):  # a function is being defined to put reversed function in it.
#     return [ele for ele in reversed(lst)]  # iterator ele will cycle through the list. Loop required.

# slicing technique:-
# In this technique, a copy of the list is made, the original list is not sorted in-place.
# Creating a copy requires more space to hold all of the existing elements. This exhausts more memory.

# Using the for loop:-
# Using for loop also, we can reverse the list, this is shown in the example.
# But remember, length of the list should not be taken full length, only half of the list length should be taken.

# -----------------------*---------------------*------------------------*--------------------------*---------------

# solution:-

# In this first step, we are creating the list using user inputs.
# input_from_user = input("Enter the calorific values with commas\n")
# list_input = input_from_user.split(",")
# print("ok, your list is", list_input)

# Another way to make list from the user input, solution from youtube:-
# size = int(input("Enter the size of the list\n"))
# list_input = []
# for items in range(size):
#     list_input.append(int(input("Enter the list element\n")))
# Remember :- Using list comprehension technique, we can avoid append(), we can write code in single line as below.
# this is simple technique    list_input = [int(input("Enter the list element\n")) for item in range(size)]
# print(f"ok, your list is {list_input}")

# first we use reverse() function to reverse the list. It reverses the list in place.
# list_input_copy = list_input[:]  # this technique just creates the copy of original list.

# Here, common errors committed by the Python programmers are given below with comments.
# Remember:- list_input_copy = list_input creates the same identity variable, so we can not use reverse function.
# Note:- Since reverse() reverses the original list, we must create the copy of the original list.
# Remember:- we can not assign another variable to the original variable since it also becomes modified.
# we can not write the below code since variable can not be assigned to the original variable.
# list_input2 = list_input_copy.reverse()  # wrong, we can not assign another variable, it also gets modified.
# print(list_input2)  # this results in "None"

# list_input_copy.reverse()  # correct method
# print("The output using the reverse method is", list_input_copy)


# now we go for reversed() function to reverse the list. We use list comprehension technique.
# print("The output using the reversed method is", [x for x in reversed(list_input)])

# conventional method is lengthy. It is given below.
# list_input2 = []  # we should create an empty list
# reversed_var = reversed(list_input)
# print(reversed_var)  # here, we get only the location of the list object.
# so we have to create an "iterator" and put it inside the loop in order to get the items.
# for item in reversed_var:
#     list_input2.append(item)  # all the items will be appended to the empty list.
# print("The output using the reversed method is", list_input2)


# Now, we go for slicing technique, it creates a copy of the list object, it won't change the original object.
# list_input3 = list_input[::-1]  # a copy of the original list is used for the operation.
# print("The output using the slicing technique is", list_input3)
# Note:- We can even write without making a variable, slicing technique copies the object automatically.
# print("The output using the slicing technique is", list_input[::-1])  # we get the same result


# Now, we go for looping technique to reverse the list object. It changes the original list.
# We can make a copy of the list and we go for loop method. In this example, we go directly. No problem.

# What happens if we take the entire length of the list??
# We can not reverse the list because reverse of reverse is the original list. This is what happens when we do.
# for x in range(len(list_input)):
#     list_input[x], list_input[len(list_input) -x -1] = list_input[len(list_input) -x -1], list_input[x]
#     print(f"at each iteration, the value of x is {x} and the list is {list_input}")  # we can easily clearly see.
# this is the most important step, here we are equating the (n,m) pair to (m,n) pair.
# we are equating (0,5),(1,4),(2,3),(3,2),(4,1),(5,0) pairs with (5,0),(4,1),(3,2),(2,3),(1,4),(0,5) pairs.
# So, reverse of reverse, we get the original list. This is the reason we should change the length by half.
# print("The output using looping technique is", list_input)

# What happens if we take the half of the length of the list?
# We get the correct answer.
# for x in range(len(list_input)//2):
#     list_input[x], list_input[len(list_input) -x -1] = list_input[len(list_input) -x -1], list_input[x]
# print("The output using looping technique is", list_input)

# --------------------*----------------------*------------------------*---------------------------*----------------
# --------------------*----------------------*------------------------*---------------------------*----------------


# Now, we learn about the concept of creating a copy of the object.
# Using [:] this technique we can create a copy of list object.


# See the below example, [:] is not used. So, all the objects will be changed after the looping process.
# list1 = [2, 4, 6, 9, 10]  # a list is written
# list_jj = list1  # another variable is assigned to the list.
# for y in range(len(list_jj)//2):
#     list_jj[y], list_jj[len(list_jj) -y -1] = list_jj[len(list_jj) -y -1], list_jj[y]
#     print(f"value of y in every step is {y} and list_jj is {list_jj}")
# print(list1)  # remember list1 will also be changed
# print(list_jj)  # since they have equal identity, both the list will be changed.


# See the below example, [:] is used. So, a copy is made and original object will not be affected.
# list1 = [2, 4, 6, 9, 10]  # a list is written
# list_jj = list1[:]  # a copy is made.
# for y in range(len(list_jj)//2):
#     list_jj[y], list_jj[len(list_jj) -y -1] = list_jj[len(list_jj) -y -1], list_jj[y]
#     print(f"value of y in every step is {y} and list_jj is {list_jj}")
# print(list1)  # remember list1 will not be changed here
# print(list_jj)

# -----------------------*----------------------*----------------------*--------------------------*----------------

# What happens if we replace only one item in the loop, see the example below.
# We can only replace half of the list, the other half will not be replaced. See the example.
list1 = [2,4,6,8,10,12]
for x in range(len(list1)):
    list1[x] = list1[len(list1) -x -1]
    print(f"in every step, value of x is {x} and the list is {list1}")
# by replacing only one item, we can not replace all the item.
# As we have seen above, only half of the list can be changed, rest half can not be changed.

# ---------------------*--------------------*-------------------------*-------------------------*------------------


