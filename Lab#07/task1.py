import threading,time

def thread1(promt):
    print(f"Hello {promt}!")
    time.sleep(5)

def thread2(promt):
    print(f"Student roll no is{promt}")
    time.sleep(5)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1,args=('Muhammad Waleed',))
    t2 = threading.Thread(target=thread2,args=('20b-115-se',))
    t1.start()
    t2.start()

    print('main thread')

    t1.join()
    t2.join()

    print('all done')
