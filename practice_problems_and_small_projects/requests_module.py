# requests module is not a built in Python module, so first we have to install using pip install.
# requests module is used to send HTTP requests from our program directly.
# Whenever we send HTTP request from our program, We get response object in return.
# HTTP - Hypertext transfer protocol (means set of methods through which client and server connection is established)
# when we request data from the server, we get response from the server.
# we can send data to the server for data processing.
# There are many built in methods in requests module, they are get(), head(), put(), delete() etc.


# get() is used to get information from any URL/site.
# syntax of get() is  requests.get(URL, shiva={key : value}, args)
# URL: this is the URL of the website where we want to send the request.
# Params: this is a dictionary or a list or tuples used to send a query string.
# Args: It is optional. It can be any named arguments offered by the get method.


import requests
# r = requests.get(https://developers.hubspot.com/docs/api) # HTTP request data should be stored into a variable.
# print(r.text) # we get the data of the website in text format. It is available in view page source.
# print(r.status_code)  # if we get 200, then request is OK.

# post() method helps to put some data into the website.
url = "www.something.com"
data = {
    "p1": 4,
    "p2": 8
}
r2 = requests.post(url=url, data=data)  # when the data is put into the website like this, we get response object.
# above we can see r.text is the response object. Here also we get the response object/information.
# print(r2.text)  # these are the responses we get from the server side.
# print(r2.status_code)  # this response we can get from the server.

# --------------------*-----------------------*------------------------------*---------------------------*----------

