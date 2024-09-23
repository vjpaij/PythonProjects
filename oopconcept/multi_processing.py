import time
import multiprocessing

# Multithreading refers to the ability of a processor to execute multiple threads
# concurrently, where each thread runs a process. Multiprocessing refers to the ability of
# a system to run multiple processors in parallel, where each processor can run one or
# more threads.

square_result = []
cube_result = []

def calc_square(number):
    print("Calculate square numbers")
    global square_result
    for n in number:
        time.sleep(0.2)
        print("square:", n*n)
        square_result.append(n*n)
    print(str(square_result))


def calc_cube(number):
    print("Calculate cube numbers")
    global cube_result
    for n in number:
        time.sleep(0.2)
        print("cube:", n*n*n)
        cube_result.append(n * n)
    print(str(cube_result))


if __name__ == "__main__":
    arr = [1,2,3,4]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
