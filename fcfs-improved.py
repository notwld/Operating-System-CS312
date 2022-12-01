import threading
import time

class Process:
    def __init__(self, arrival_time=0, burst_time=0):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turn_around_time = 0
        self.completion_time = 0
        self.prev = None

total_avg_waiting_time=0
total_avg_turn_around_time=0

def core_one(processes):
    global total_avg_turn_around_time,total_avg_waiting_time
    avg_waiting_time=0
    avg_turn_around_time=0
    index = 0
    prev = None
    for process in processes:

        print(f"""
    P{index+1}\t\t\t{process.arrival_time}\t\t\t{process.burst_time}\t\t\t{process.burst_time if prev is None else prev+process.burst_time}\t\t\t{process.burst_time if prev is None else (prev+process.burst_time)-process.arrival_time}\t\t\t{(process.burst_time if prev is None else (prev+process.burst_time)-process.arrival_time) - process.burst_time}
        """)
        process.waiting_time = process.turn_around_time - process.burst_time
        prev = process.burst_time if prev is None else prev+process.burst_time
        process.completion_time = prev
        process.turn_around_time = process.burst_time if prev is None else (
            prev+process.burst_time)-process.arrival_time
        avg_waiting_time += process.waiting_time
        avg_turn_around_time += process.turn_around_time
        index += 1
    print()
    print("Avg. Waiting Time: ",abs(avg_waiting_time/len(processes)))
    print("Avg. Turn Around Time: ",avg_turn_around_time/len(processes))
    total_avg_waiting_time += abs(avg_waiting_time/len(processes))
    total_avg_turn_around_time += avg_turn_around_time/len(processes)

def core_two(processes):
    global total_avg_turn_around_time,total_avg_waiting_time
    avg_waiting_time=0
    avg_turn_around_time=0
    index = 0
    prev = None
    for process in processes:

        print(f"""
    P{index+1}\t\t\t{process.arrival_time}\t\t\t{process.burst_time}\t\t\t{process.burst_time if prev is None else prev+process.burst_time}\t\t\t{process.burst_time if prev is None else (prev+process.burst_time)-process.arrival_time}\t\t\t{(process.burst_time if prev is None else (prev+process.burst_time)-process.arrival_time) - process.burst_time}
        """)
        process.waiting_time = process.turn_around_time - process.burst_time
        prev = process.burst_time if prev is None else prev+process.burst_time
        process.completion_time = prev
        process.turn_around_time = process.burst_time if prev is None else (
            prev+process.burst_time)-process.arrival_time
        avg_waiting_time += process.waiting_time
        avg_turn_around_time += process.turn_around_time
        index += 1
    print()
    print("Avg. Waiting Time: ",abs(avg_waiting_time/len(processes)))
    print("Avg. Turn Around Time: ",avg_turn_around_time/len(processes))
    total_avg_waiting_time += abs(avg_waiting_time/len(processes))
    total_avg_turn_around_time += avg_turn_around_time/len(processes)

processes = []
threads=[]
process = int(input("Enter total number of processes (maximum 20) :"))
for each in range(0, process):
    burst_time = int(input(f"Enter burst time of P[{each+1}]: "))
    processes.append(Process(burst_time=burst_time))

mid = len(processes)//2
t1 = threading.Thread(target=core_one,args=(processes[:mid],))
t2 = threading.Thread(target=core_two,args=(processes[mid:len(processes)],))
threads.append(t1)
threads.append(t2)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print("Total Avg. Waiting Time:",total_avg_waiting_time)
print("Total Avg. Turn Around Time:",total_avg_turn_around_time)