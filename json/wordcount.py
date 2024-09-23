"""
modes for file:
r: reading the file
w: writing into a file
a: appends to a file
r+: used for both read and write into the file. The file name should be present before
w+: used for both read anf write into the file. Creates file name if not present before
"""


r = open("/Users/in22417145/PycharmProjects/json/book.txt","r")
#print(r.read())
#r.close()

#when we use for loop on file, it reads line by line

for line in r:
    print(line)
    # below line gives me a List with each words from a line
    tokens = line.split(" ")
    print(tokens)
    print(str(tokens))
    print(len(tokens))

r.close()