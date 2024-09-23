numbers = [1,2,3,4,5,6,7,8]
even = []

for i in numbers:
    if i % 2 ==0:
        even.append(i)

#list comprehensions
even_comp = []
even_comp = [i for i in numbers if i % 2 == 0]
print((even_comp))

square = [i*i for i in numbers]
print(square)

#set comprehensions
#set is similar to lists but would remove duplicates and give unordered collection of
#unique records
#set doesnt index operations i.e s[0] throws error as these unordered
#iteration is allowed i.e for i in s: print(i)
# set initialisation is s= (). not s= {} as curly braces are for dictionary initialisation


s = set((1,2,3,4,5,1,3))
print(s)
print(type(s))

even_set = {i for i in numbers if i % 2 == 0}
print(even_set)

#dictionary comprehension
cities = ["mumbai", "tokyo", "new york", "london"]
countries = ["india","japan","usa","uk"]
#zip is a function which zips 2 list together

z = zip(cities, countries)
for a in z:
    print(a)
# ('mumbai', 'india')
# ('tokyo', 'japan')
# ('new york', 'usa')
# ('london', 'uk')

d = {city:country for city,country in zip(cities,countries)}
print(d)
# {'mumbai': 'india', 'tokyo': 'japan', 'new york': 'usa', 'london': 'uk'}