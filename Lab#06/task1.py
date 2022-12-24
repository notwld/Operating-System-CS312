#!/bin/python3

import os,time

id=os.fork()
if id == 0:
    print("The child is running")
    time.sleep(10)
else:
    print("The parent is running")
    os.wait()

