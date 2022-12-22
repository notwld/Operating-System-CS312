import threading
import random
import time,os

try:
    from rich.console import Console
    from rich.table import Table
    import pyfiglet as pyg  
except ImportError:
    import os 
    os.system("pip install rich")
    os.system("pip install pyfiglet")
    from rich.console import Console
    from rich.table import Table
    import pyfiglet as pyg  

os.system("clear")
buf = []
empty = threading.Semaphore(5)
full = threading.Semaphore(0)
mutex = threading.Lock()

def pretty_print(empty, full, num):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Empty", style="dim", width=12)
    table.add_column("Full", style="dim", width=12)
    table.add_column("Mutex", style="dim", width=12)
    table.add_row(str(empty._value), str(full._value), str(num))
    console.print(table)

def producer(pname):
    empty.acquire()
    mutex.acquire()         # added
    print("Producing",pname)
    pretty_print(empty, full, 1)
    mutex.release()         # added
    full.release()



def consumer(cname):
    full.acquire()
    mutex.acquire()         # added
    print("Consuming",cname)
    pretty_print(empty, full, 1)
    mutex.release()         # added
    empty.release()



seq = ['C1','P1','P2','P3','C2','P4','P5','P6','P7']
threads = []
for i in seq:
    if 'C' in i:
        threads.append(threading.Thread(target=consumer,args=(f'{i}',)))
    else:
        threads.append(threading.Thread(target=producer,args=(f"{i}",)))

for t in threads:
    t.start()