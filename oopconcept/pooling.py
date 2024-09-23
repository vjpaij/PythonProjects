from multiprocessing import Pool
import time

#Pooling divides the work to all the cores in CPU and hence in fast processing

def f(n):
    sum = 0
    #for x in range(1,1000):
    for x in range(1,100000):
        sum += x*x
    print("function sum:", sum)

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(1,2))
    p.close()
    p.join()

    print("Pool took", time.time() - t1)

    t2 = time.time()
    sum = 0
    #result = []
    for x in range(100000):
        sum += x * x
    print("sum outside:",sum)
        #result.append(f(x))

    print("Serial processing took", time.time() - t2)
