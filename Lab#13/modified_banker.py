import sys
import random


class Banker:
    def __init__(self, num_resources, num_processes, _max, allocation, available):
        self._max = _max
        self.allocation = allocation
        self.available = available
        self.need = []
        self.num_resources = num_resources
        self.num_processes = num_processes
        self.calculate_need()

    def calculate_need(self):
        for i in range(len(self._max)):
            for j in range(self.num_resources):
                self.need.append(self._max[i][j]-self.allocation[i][j])
        self.need = [self.need[i:i+self.num_resources] for i in range(0, len(self.need), self.num_resources)]

    def safe_state(self):
        work = self.available
        finish = [False for i in range(len(self.need))]
        sequence = []
        while False in finish:
            for i in range(len(self.need)):
                for j in range(len(self.need[i])):
                    if self.need[i][j] <= work[j] and finish[i] == False:
                        work[j] += self.allocation[i][j]
                        finish[i] = True
                        sequence.append(f"p{i+1}")
        return sequence

    def request_resources(self, process, request):
        if request[0] > self.need[process][0] or request[1] > self.need[process][1] or request[2] > self.need[process][2]:
            print("Error: Request exceeds need")
            return False
        elif request[0] > self.available[0] or request[1] > self.available[1] or request[2] > self.available[2]:
            print("Error: Request exceeds available")
            return False
        else:
            for i in range(self.num_resources):
                self.available[i] -= request[i]
                self.allocation[process][i] += request[i]
                self.need[process][i] -= request[i]
            if self.safe_state() == False:
                for i in range(self.num_resources):
                    self.available[i] += request[i]
                    self.allocation[process][i] -= request[i]
                    self.need[process][i] += request[i]
                print("Error: Request results in unsafe state")
                return False
            else:
                print("Request granted")
                return True

    def table(self):
        print("Process\t\tMax\t\tAllocation\tNeed\t\tAvailable")
        for i in range(len(self._max)):
            print(
                f"P{i+1}\t\t{self._max[i]}\t{self.allocation[i]}\t{self.need[i]}\t{self.available}")


if __name__ == "__main__":
    num_resources = int(sys.argv[1])
    num_processes = int(sys.argv[2])
    _max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    available = [3, 3, 2]
    banker = Banker(num_resources, num_processes,_max, allocation, available)
    banker.table()

    print("Safe sequence: ", banker.safe_state())

    print("Safe sequence: ", banker.safe_state())

    banker.request_resources(0, [0, 1, 0])
    banker.table()
