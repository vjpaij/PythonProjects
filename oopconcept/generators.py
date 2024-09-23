def fibonacci():
    a,b = 0,1

    while True:
        #yield is similar to return but it continues to later statements
        yield a
        a,b = b, b+a


#below code iterates through each value given out by yield
for n in fibonacci():
    if n > 10000:
        break
    print(n)
