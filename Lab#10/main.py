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

def pretty_print(empty, full, num,buf):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Buffer", style="dim", width=12)
    table.add_column("Empty", style="dim", width=12)
    table.add_column("Full", style="dim", width=12)
    table.add_column("Value", style="dim", width=12)
    table.add_row(str(buf), str(empty._value), str(full._value), str(num))
    console.print(table)

def producer(pname):
    nums = range(5)
    global buf,empty,full
    num = random.choice(nums)
    empty.acquire()
    mutex.acquire()         # added
    buf.append(num)
    print("Producing",pname)
    pretty_print(empty, full, num, buf)
    mutex.release()         # added
    full.release()



def consumer(cname):
    global buf,empty,full
    full.acquire()
    mutex.acquire()         # added
    num = buf.pop(0)
    print("Consuming",cname)
    pretty_print(empty, full, num, buf)
    mutex.release()         # added
    empty.release()



seq = ['C1','P1','P2','P3','C2','P4','P5','P6','P7']
threads = []
for i in seq:
    if i[0] == 'C':
        t = threading.Thread(target=consumer, args=(i,))
        threads.append(t)
    else:
        t = threading.Thread(target=producer, args=(i,))
        threads.append(t)

for t in threads:
    t.start()