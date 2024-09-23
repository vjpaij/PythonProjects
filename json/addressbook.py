book = {}

book["vijay"] = {
    "name": "vijay",
    "location" : "bengaluru",
    "phone" : 1234512345
}

book["vinay"] = {
    "name": "vinay",
    "location" : "mumbai",
    "phone" : 9234512349
}

print(book)

import json

#dumps coverts the object (in this case a dictionary type) to string
s = json.dumps(book)
print(s)

with open("/Users/in22417145/PycharmProjects/json/book.txt","w") as f:
#can also be written as below:
# f= open("/Users/in22417145/PycharmProjects/json/book.txt","w")
#when we give it as "with" statement, explicit closing of file is not required.
# i.e. f.close() need not be mentioned
    f.write(s)
    

