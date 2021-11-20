# Task name :- Pickling Iris
# In this task, we need Iris dataset. It's available in  https://archive.ics.uci.edu/ml/index.php
# In Iris data folder, download iris.data file.
# After downloading the iris.data file, parse it using any method.
# Use requests module and also required functions to get the original list object.

# ----------------------*-------------------*--------------------*-------------------*------------------*-------------
# solution:-

# import pickle
# import requests
# import json

# requesting_iris = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# content = requesting_iris.content  # we get the response in text format using content command.
# content variable has all the information of the iris data, this should be written inside a file.

# with open("iris.data", "wb") as file:
#     file.write(content)  # content will be written inside the "iris.data" file.
# with open("iris.data", "rt") as file2:  # now, the same iris data will be opened for reading the data.
#     datalines = file2.readlines()  # iris data file content is read line by line, output will be in list format.
#     print(datalines[0:4])
#     result = []  # create an empty list, later items will be appended into the list.
#     for x in datalines:  # x means lines in datalines.
#         list_output = x.split(",")  # using split function, we can get the output as list of lists.
#         result.append(list_output)  # using append() function, we can add the items to empty list.
#     print(result)

# First part is over, now we should do pickling.
# with open("result.pkl", "wb") as my_file:
#     pickle.dump(result, my_file)  # send both object and file object as arguments inside dump() function.

# retrieve_list = None  # if at all file is corrupted, then we need to print "None".
# with open("result.pkl", "rb") as my_file2:  # using file pointer, we can open the same pickled file.
#     retrieve_list = pickle.load(my_file2)  # using load() the object is retrieved back.

# print(retrieve_list)  # we get the same list what we had pickled.

# ----------------------------*------------------------*--------------------*---------------------------*-------------

# another solution from Youtube:-

import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)
l1 = data.split("\n")  # split() function splits the items and gives the result in list format.
# print(l1)
# Remember: we can not split the "l1" list using split() function since there is no clarity.
l2 = [item.split(",") for item in l1 if len(item) != 0]  # instead of append(), use list comprehension technique.
print(l2)  # we get the list of lists as the output.

# Now, pickling part will start.
with open("myiris.pkl", "wb") as myfile:  # file object required to open the file in program.
    pickle.dump(l2, myfile)  # dump() function needs both object and file object as arguments.
with open("myiris.pkl", "rb") as myfile2:  # file pointer/ file object is required to open the file in program.
    original_l2 = pickle.load(myfile2)
    print(original_l2)  # we get back the original list.

# ------------------------*--------------------*-------------------*--------------------------------*---------------
