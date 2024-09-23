import time
import threading

def calc_square(number):
    print("Calculate square numbers")
    for n in number:
        time.sleep(0.2)
        print("square:", n*n)

def calc_cube(number):
    print("Calculate cube numbers")
    for n in number:
        time.sleep(0.2)
        print("cube:", n*n*n)

arr = [1,2,3,4]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args= (arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in :", time.time() - t)

