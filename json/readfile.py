import json

r = open("/Users/in22417145/PycharmProjects/json/book.txt","r")
str1 = r.read()
r.close()
print(str1)
print(type(str1))

addr = json.loads(str1)
print(addr)
print(type(addr))


#print location of vinay

print(addr["vinay"]["location"])

for name in addr:
    print(addr[name])

