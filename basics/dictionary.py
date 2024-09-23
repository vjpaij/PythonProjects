d = {"Karnataka":"Bengaluru", "Kerala":"Thiruvananthapuram","Goa":"Panaji"}
print(d)

print(d["Goa"])

d["Tamil Nadu"] = "Chennai"
print(d)

del d["Kerala"]
print(d)

for key in d:
    print("State:",key,"Capital:",d[key])
#or it can also be written as below
for k,v in d.items():
    print("State:",k,"Capital:",v)

#Gives True or False if key is present in the dictionary
print("Goa" in d)
print("Sikkim" in d)

#to clear the dictionary
d.clear()

