# to take out particular pattern from a string, we need regular expressions.
# by writing import re, we can easily import built in regular expressions module.


# here we first understand something about raw string.
# if we put raw string, then it will not allow escape sequence character to get escaped from the print.
# for example:-  print(r"\n")   # "\n" will be printed by putting raw string.


# in this example, we take a docstring with certain characters assigned to a variable. It's a multiline string.
# import re  # regular expressions module imported

# mystr = '''Tata Limited
# Dr. David Landsman, executive director
# 18, Grosvenor Place
# London SW1X 7HSc
# Phone: +44 (20) 7235 8281
# Fax: +44 (20) 7235 8727
# Email: tata@tata.co.uk
# Website: www.europe.tata.com
# Directions: View map

# Tata Sons, North America
# 1700 North Moore St, Suite 1520
# Arlington, VA 22209-1911
# USA
# Phone: +1 (703) 243 9787
# Fax: +1 (703) 243 9791
# 66-66
# 455-4545
# Email: northamerica@tata.com
# Website: www.northamerica.tata.com
# Directions: View map'''

# findall, search, sub, split, finditer are the main functions present in re module.
# metacharacters, special sequences are the concepts which are used in re for the complicated search works.


# here is an example of a normal search work done using re and for loop.

# first, we should define the pattern we want to search, it is done using re.compile function.
# assign the defined pattern to a variable.
# later we can use finditer function to search the pattern.

# patt = re.compile(r"fass")  # here we are searching the pattern "fass"
# matches = patt.finditer(mystr)  # put the content variable inside the finditer function to get the results/matches.
# for item in matches:
#     print(item)  # we don't get any matches because there is no string with "fass"
# patt2 = re.compile(r"on")
# matches2 = patt2.finditer(mystr)
# for match in matches2:
#     print(match)  # we get the result for all objects locations    <re.Match object; span=(73, 75), match='on'>
# print(mystr[73:75])  # this is what span gives the information about the characters, we get the matched item.

# this kind of searching we can easily do using loops. But using re module we can even search complicated things.

# ----------------------------*----------------------------*--------------------------------*---------------------

# using metacharacters and special sequence concept, we can search complicated things in re module.

# import re
# mystr = '''Tata Limited
# Dr. David Landsman, executive director
# 18, Grosvenor Place
# London SW1X 7HSc
# Phone: +44 (20) 7235 8281
# Fax: +44 (20) 7235 8727
# Email: tata@tata.co.uk
# Website: www.europe.tata.com
# Directions: View map

# Tata Sons, North America
# 1700 North Moore St, Suite 1520
# Arlington, VA 22209-1911
# USA
# Phone: +1 (703) 243 9787
# Fax: +1 (703) 243 9791
# 66-66
# 455-4545
# Email: northamerica@tata.com
# Website: www.northamerica.tata.com
# Directions: View map'''

# patt = re.compile(r".")  # we get all the characters except new line character.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get all the characters details, dot stands for all the characters.

# patt = re.compile(r".on")  # we get 3 characters, first will be any character and the next two will be "on"
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get the result with any character with "on"  <re.Match object; span=(72, 75), match='Lon'>

# patt = re.compile(r"^or")  # ^ string Starts with symbol, this is a metacharacter.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # it won't return anything because "mystr" string doesn't start from "or" keyword.

# patt = re.compile(r"^Tata")  # ^ string Starts with symbol, this is a metacharacter.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # it gives the result    <re.Match object; span=(0, 4), match='Tata'>

# patt = re.compile(r"ma$")  # ^ string Ends with symbol, this is a metacharacter.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we don't get result because string doesn't end with "ma"

# patt = re.compile(r"ap$")  # ^ string Ends with symbol
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get the result as    <re.Match object; span=(445, 447), match='ap'>

# patt = re.compile(r"a*")  # * gives Zero or more occurrences, it is put after the required pattern
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # it gives just a space to other characters/zero "a", and if there is one or more than one "a"
# these are some of the results, we get space for every other character, and we get one or more than one "a"
# <re.Match object; span=(0, 0), match=''>  <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 2), match=''>  <re.Match object; span=(3, 4), match='a'>

# patt = re.compile(r"a*t*")  # zero or all a, zero or all t, zero or all at
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# patt = re.compile(r"w+")  # + gives one or more occurrences
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)
# few results <re.Match object; span=(171, 174), match='www'>  <re.Match object; span=(206, 207), match='w'>

# patt = re.compile(r"w{3}")  # {} gives Exactly the specified number of occurrences
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get the info of pattern where we have exactly  3 w
# few results <re.Match object; span=(171, 174), match='www'>  <re.Match object; span=(401, 404), match='www'>

# patt = re.compile(r"(.ww){1}")  # () Capture and group, {} Exactly the specified number of occurrences
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)
# we get   <re.Match object; span=(170, 173), match=' ww'>    <re.Match object; span=(400, 403), match=' ww'>

# patt = re.compile(r"(ww){1}|(com){1}")  # | gives Either or
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # gives ww occurred 1 time, com occurred 1 time.

# ------------------------*--------------------------*-------------------------*-------------------*---------------

# Now, we will look into special sequence characters.

import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map'''

# patt = re.compile(r"\ATat")  # \A Returns a match if the specified characters are at the beginning of the string
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # <re.Match object; span=(0, 3), match='Tat'>

# patt = re.compile(r"\bTat")  # \b Returns a match if the specified characters are at the beginning or at the end.
# Remember:- It gives matches in between the string also.
# If \b is put before the Tat, gives matches which are at the beginning.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # <re.Match object; span=(0, 3), match='Tat'>  <re.Match object; span=(213, 216), match='Tat'>

# patt = re.compile(r"tata\b")  # \b Returns a match if the specified characters are at the beginning or at the end.
# Remember:- It gives matches in between the string also.
# If \b is put after the tata, gives matches which are at the end.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # so we get 5 results which has tata.

# patt = re.compile(r"\d{4}")  # \d Returns a match where the string contains digits (numbers from 0-9)
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get pattern which has 4 digits. So we get 11 search results.

# patt = re.compile(r"\d{5}-\d{4}")  # \d Returns string with digits (numbers from 0-9)
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get pattern which has 5 digits 1 dash 4 digits, So we get 1 result.

# patt = re.compile(r"1{2}\b")  # 1 occurred 2 times and it should match from the end.
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)  # we get one result  <re.Match object; span=(292, 294), match='11'>

# ---------------------*-------------------------------*---------------------------*------------------------------

