import threading,os,time

readcount = 0
mutex = threading.Lock()
wrt = threading.Lock()

def reader():
    global readcount
    print("Reader arrived")
    mutex.acquire()
    readcount += 1
    if readcount == 1:
        wrt.acquire()
    mutex.release()
    print("Reader is reading")
    mutex.acquire()
    readcount -= 1
    if readcount == 0:
        wrt.release()
    mutex.release()
    time.sleep(2)

def writer():
    print("Writer arrived")
    wrt.acquire()
    print("Writer is writing")
    wrt.release()
    time.sleep(1)

writer = threading.Thread(target=writer)

reader1 = threading.Thread(target=reader)
reader2 = threading.Thread(target=reader)
reader3 = threading.Thread(target=reader)

writer.start()
reader1.start()
reader2.start()
reader3.start()

writer.join()
reader1.join()
reader2.join()
reader3.join()





