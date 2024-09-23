num = input("enter a number:")

#input entered from console will be a string. So convert it to num
num = int(num)

if num%2 == 0:
    print("number is even")
else:
    print("number is odd")

asia = ["India", "China", "Pakistan", "UAE"]
europe = ["UK", "Czech Republic", "Hungary", "Poland"]
africa = ["South Africa", "Nigeria", "Sudan", "Egypt"]

country = input("Enter the country name:")

if country in asia :
    print("Country is in Asia")
elif country in europe :
    print("Country is in Europe")
elif country in africa :
    print("Country is in Africa")
else :
    print("Country not in database")
