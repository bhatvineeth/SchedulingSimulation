import math

from pip._vendor.distlib.compat import raw_input

p = 0


def printSequence(processes, n):
    execution = []
    for i in range(0, n):
        execution.append(processes[i][0])
    LCM = max((map(lambda x: x[1], processes)))
    while 1:
        ind = 0
        for j in range(0, n):
            if LCM % processes[j][1] == 0:
                ind = ind + 1
        if ind == n:
            break
        else:
            LCM = LCM + 1
    Result = []
    for i in range(0, LCM):
        if i != 0:
            for k in range(0, n):
                if i % processes[k][1] == 0:
                    execution[k] = processes[k][0]
        ind = 0
        for j in range(0, n):
            if execution[j] != 0:
                execution[j] = execution[j] - 1
                Result.append(j + 1)
                ind = 1
                break
        if ind == 0:
            Result.append(-1)

    for i in range(0, LCM):
        if Result[i] != - 1:
            print("From% d to% d: p% d " % (i, i + 1, Result[i]))
        else:
            print(" From% d to% d: Empty slot " % (i, i + 1))

    return


n = input(" Enter No. of processes: ")
n = int(n)
processes = []
print(" Enter Execution time and Period of Processes ")
for i in range(0, n):
    pair = []
    input_1 = raw_input()
    Ex, Period = input_1.split()
    pair.append(int(Ex))
    pair.append(int(Period))
    processes.append(pair)
processes.sort(key=lambda x: x[1])
print(processes)
u = 0
for j in range(0, n):
    u = u + processes[j][0] / float(processes[j][1])
print("Utilization:% f" % (u))
if u <= 1:
    Ub = n * (pow(2, 1 / float(n)) - 1)
    if u <= Ub:
        print("processes are schedulable")
        printSequence(processes, n)
    else:
        ind = 0
        ind1 = 0
        success = 1
        for k in range(1, n):
            R = 0
            for j in range(0, k + 1):
                R = R + processes[j][0]
            R1 = processes[k][0]
            while (1):
                i = k - 1
                while (i >= 0):
                    R1 = R1 + (math.ceil(R / float(processes[i][1]) * processes[i][0]))
                    i = i - 1
                if R1 > processes[k][1]:
                    ind = 1
                    ind1 = k
                    break
                if R1 == R:
                    break
                else:
                    R = R1
                    R1 = processes[k][0]
            if ind == 1:
                print("Processes are not schedulable since processes% d can't meet deadline" % (ind1))
                success = 0
                break
        if success == 1:
            print("processes are schedulable")
            printSequence(processes, n)
else:
    print("processes are not schedulable")
