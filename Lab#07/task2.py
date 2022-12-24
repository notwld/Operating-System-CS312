import threading,random,time

def displayMsg(msg):
    print(msg)

if __name__ == '__main__':
    threads = []
    n = int(input("Enter number of threads: "))
    for i in range(n):
        threads.append(threading.Thread(target=displayMsg, args=(f"[Thread {i+1}]: Dice {random.randint(1,6)}",)))

    for i in range(n):
        threads[i].start()
        time.sleep(1)

    for i in range(n):
        threads[i].join()

