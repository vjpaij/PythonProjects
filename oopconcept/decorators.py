import time
# to know the time taken by each function, we can add some logic into these functions.
# but this would clutter the function and also have other logic other than what the
#function was actually meant to do.
#for that we create decoraters as below


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start)*1000) + "mil secs")
        return result
    return wrapper


@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    print(result)


@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number* number)
    print(result)


array = range(1,1000)
out_square = calc_square(array)
out_cube = calc_cube(array)