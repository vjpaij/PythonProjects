num = [10,40,45,78,64,43,234]
#total = num[0]+num[1]+num[2]+num[3]+num[4]+num[5]+num[6]

total = 0
for x in num:
    total = total + x
print(total)

for i in range(10):
    print(i)

for n in range(2,5):
    print(n)

for v in range(-15,10,2):
    print(v)

num = [10,40,45,78,64,43,234]
total=0
for a in range(len(num)):
    print("number",(a+1),"is", num[a])
    total = total + num[a]
print(total)

key_location = "chair"
locations = ["sofa","table","stool","chair","mirror"]

for z in locations:
    if z==key_location:
        print("Found key", z)
        break
    else :
        print("Key not found in", z)
#break statement will come out of for loop

for q in range(1,6):
    if q%2 == 0:
        continue
    print(q*q)
#continue statement will take it back to for without executing statements below continue








