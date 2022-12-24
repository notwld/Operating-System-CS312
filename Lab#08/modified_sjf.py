import os
try:
    from rich.console import Console
    from rich.table import Table
except ModuleNotFoundError:
    os.system("pip install rich")
    from rich.console import Console
    from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")
os.system("cls")

nprocess = int(input("Enter number of processes: "))
processes = []
Sorted = []
CT = []
TAT = []
WT = []
for i in range(nprocess):
    a = int(input("Arrival time: "))
    b = int(input("Burst Time: "))
    processes.append(["P"+str(i+1), a, b])

n = len(processes)
# arranging
t = min(processes, key=lambda x: x[1])
t = t[1]
for i in range(n):
    reach_pro = []
    flag = True
    while flag == True:
        for j in range(len(processes)):
            if processes[j][1] <= t:
                reach_pro.append(processes[j])
        if len(reach_pro) == 0:
            t += 1
        else:
            flag = False
    least_bt = min(reach_pro, key=lambda x: x[2])
    t = t + least_bt[2]
    Sorted.append(least_bt)
    processes.remove(least_bt)


# Calculting Completion time
for i in range(len(Sorted)):
    if i == 0:
        if Sorted[i][1] > 0:
            state_idle = Sorted[i][1]
            CT.append(Sorted[i][2]+state_idle)
        else:
            CT.append(Sorted[i][2])
    else:
        if CT[i-1] < Sorted[i][1]:
            idle_state = Sorted[i][1] - CT[i-1]
            CT.append(CT[i-1]+Sorted[i][2]+idle_state)
        else:
            CT.append(CT[i-1]+Sorted[i][2])

# Calculation Turn Around Time
for i in range(len(Sorted)):
    TAT.append(CT[i]-Sorted[i][1])

# Calculation Waiting Time
for i in range(len(Sorted)):
    WT.append(TAT[i]-Sorted[i][2])

table.add_column("Process", justify="center")
table.add_column("Arrival Time", justify="center")
table.add_column("Burst Time", justify="center")
table.add_column("Completion Time", justify="center")
table.add_column("Turn Around Time", justify="center")
table.add_column("Waiting Time", justify="center")

for i in range(len(Sorted)):
    table.add_row(str(Sorted[i][0]), str(Sorted[i][1]), str(
        Sorted[i][2]), str(CT[i]), str(TAT[i]), str(WT[i]))


console.print(table)

print("Avarege TAT: ", round(sum(TAT)/len(TAT), 2))
print("Avarege WT: ", round(sum(WT)/len(WT), 2))
