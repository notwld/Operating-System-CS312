class Process:
    def __init__(self, arrival_time=0, burst_time=0):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turn_around_time = 0
        self.completion_time = 0
        self.prev = None


processes = []
process = int(input("Enter total number of processes (maximum 20) :"))
for each in range(0, process):
    burst_time = int(input(f"Enter burst time of P[{each+1}]: "))
    processes.append(Process(burst_time=burst_time))

print("""
Process\t\tArrival Time\t\tBurst Time\t\tCompletion Time\t\tTurn Around Time\t\tWaiting Time
""")
index = 0
prev = None
avg_waiting_time = 0
avg_turn_around_time=0
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