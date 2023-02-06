from multiprocessing import Process, Array
import random

def calculate_squares(arr, start, end):
    for i in range(start, end):
        arr[i] = arr[i] ** 2

if __name__ == '__main__':
    numbers = Array('i', [random.randint(0, 10) for _ in range(10)])
    print("Original numbers:", numbers[:])
    p1 = Process(target=calculate_squares, args=(numbers, 0, 5))
    p2 = Process(target=calculate_squares, args=(numbers, 5, 10))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Squared numbers:", numbers[:])