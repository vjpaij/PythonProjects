import time
import multiprocessing

# if variables value has to be shared between different processes, it should be stored in
#shared memory. By this, you need not have to define global variable inside a local.

# lock functionality is to lock the value of a variable when the same variable is used in
# multiple processes and hence to avoid discrepancies

def deposit(balance, lock):
    for i in range(1,100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdrawal(balance, lock):
    for i in range(1,100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":
    # i is datatype i.e. integer in this case
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdrawal, args=(balance, lock))

    d.start()
    w.start()
    d.join()
    w.join()

    print(balance.value)