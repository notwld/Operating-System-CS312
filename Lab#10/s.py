import threading,os

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    os.system("pip install rich")
    from rich.console import Console
    from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")

buf = [] 
empty = threading.Semaphore(5)
full = threading.Semaphore(0) 
mutex = threading.Lock()

table.add_column("Name", style="dim", width=12)
table.add_column("Full", style="dim", width=12)
table.add_column("Empty", style="dim", width=12)

 
def producer(name): 
    empty.acquire() 
    mutex.acquire() # added 
    print("Before name: {} Full: {} Empty: {}".format(name,full._value,empty._value))
    print("Producer is producing") 
    mutex.release() # added 
    full.release()
    print("After name: {} Full: {} Empty: {}".format(name,full._value,empty._value))
    table.add_row(name, str(full._value), str(empty._value))
    
def consumer(name): 
    full.acquire() 
    mutex.acquire() # added 
    print("Before name: {} Full: {} Empty: {}".format(name,full._value,empty._value))
    print("Consumer is consuming") 
    mutex.release() # added 
    empty.release() 
    print("After name: {} Full: {} Empty: {}".format(name,full._value,empty._value))
    table.add_row(name, str(full._value), str(empty._value))
    
threads=[]
threads.append(threading.Thread(target=consumer,args=("c1",)))
threads.append(threading.Thread(target=producer,args=("p1",)))
threads.append(threading.Thread(target=producer,args=("p2",)))
threads.append(threading.Thread(target=producer,args=("p3",)))
threads.append(threading.Thread(target=consumer,args=("c2",)))
threads.append(threading.Thread(target=producer,args=("p4",)))
threads.append(threading.Thread(target=producer,args=("p5",)))
threads.append(threading.Thread(target=producer,args=("p6",)))
threads.append(threading.Thread(target=producer,args=("p7",)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

console.print(table)