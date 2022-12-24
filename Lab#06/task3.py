#!/bin/python3

import os, time

arr = [1, 3, 2, 5, 4]
parent = os.fork()

if parent == 0:
    print("Child is running")
    print("Sorting...")
    arr.sort()
    print("Sorted array: ", arr)
else:
    print("Parent is running")
    print("Array initialized")
    os.wait()
