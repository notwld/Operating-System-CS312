#!/bin/python3

import os,time

created_processes = []

parent = os.fork()

if parent == 0:
    child_1 = os.fork()
    if child_1 == 0:
        print("Child is running with pid ", os.getpid())
    else:
        status = os.wait()
        created_processes.append(status[0])
        print("Parent is running with pid ", os.getpid())
        child_2 = os.fork()
        if child_2 == 0:
            print("Child is running with pid ", os.getpid())
        else:
            status = os.wait()
            created_processes.append(status[0])
else:
    status = os.wait()
    created_processes.append(status[0])
    print("Parent is running with pid ", os.getpid())
    child_3 = os.fork()
    if child_3 == 0:
        print("Child is running with pid ", os.getpid())
    else:
        status = os.wait()
        created_processes.append(status[0])
        print("Parent is running with pid ", os.getpid())
        created_processes.append(os.getpid())
        print("Created processes: ", created_processes)


