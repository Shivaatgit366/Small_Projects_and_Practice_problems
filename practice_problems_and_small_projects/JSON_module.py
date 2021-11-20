# JSON - Javascript Object Notation, it is used storing, transferring data interacting with internet.
# JSON is similar to Python dictionary, it is a unordered collection of key and value pairs.
# In JSON, keys are unique strings which can not be null.
# In JSON, values can be anything like string, tuple, number, boolean, list or null.
# A JSON is represented by a string which is enclosed within curly braces { } with key-value pairs.
# we have to import JSON module using import keyword.

# below is the example of JSON data.
# {"name": "harry", "salary": 9000, "language": "Python"}  # key is string and value can be any data type.

# Remember:-
# If the JSON string is converted to Python, it becomes Python dictionary.
# "Parsing" is the word used for conversion of data from JSON to Python.

# Methods used for parsing of the data:-
# load() - this method is used to load JSON file data into a Python dictionary.
# loads() - this method is used to load JSON variable data into a Python dictionary.
# dump() - this method is used to load Python dictionary data into JSON file.
# dumps() - this method is used to load Python dictionary data into JSON variable.


# following is the simple example showing the usage of JSON package in Python.
# import json  # json is in small letters
# a = {"name": "shiva", "salary": 400000, "language": "Python"}  # a Python dictionary.
# b = json.dumps(a) # using dumps() method, we convert dictionary data into a JSON variable "b".
# print(b)  # we get the output as    {"name": "shiva", "salary": 400000, "language": "Python"}


# If data in JSON is true, then data in Python is true.
# If data in JSON is false, then data in Python is false.
# If data in JSON is string, then data in Python is string.
# If data in JSON is number, then data in Python is number.
# If data in JSON is array, then data in Python is list or tuple.
# If data in JSON is object, then data in Python is dictionary.
# If data in JSON is null, then data in Python is none.


# import json
# In this below example we will use the loads() method and parse the data from javascript to python.
# data = '{"var1":"shiva", "var2":2000}'  # this is Javascript string/JSON object. Put only single quotes.
# we can not write like this   print(data["var1"]) since it is a string
# using loads method we will convert the javascript string into Python.
# parsed = json.loads(data)
# print(parsed["var1"])  # we get the output  shiva
# print(type(parsed))  # <class 'dict'>


# we look into another example how a Python dictionary is converted into JSON variable.
# import json
# data2 = {
#     "channel_name": "CodeWithHarry",
#     "cars": ['bmw', 'audi a8', 'ferrari'],
#     "fridge": ('roti', 540),
#     "isbad": False  # capital F will be converted into small f.
# }
# jscomp = json.dumps(data2)  # using dumps() method, we convert Python dictionary data into javascript variable.
# print(jscomp)  # we can use "inspect element" in chrome browser for testing this example.
# the output will be
# {"channel_name": "CodeWithHarry", "cars": ["bmw", "audi a8", "ferrari"], "fridge": ["roti", 540], "isbad": false}

# ------------------*----------------*------------------*-------------------------*--------------------*------------
