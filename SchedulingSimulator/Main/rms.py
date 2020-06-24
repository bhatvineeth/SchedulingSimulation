import math


def printSequence(processes, n, logFile):
    execution = []
    startingPoints = []
    tasksArray = []
    resultArray = []
    arrivalArray = []
    for i in range(0, n):
        execution.append(processes[i][0])
        arrivalArray.append(processes[i][2])
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
                if abs(i - processes[k][2]) % processes[k][1] == 0:
                    execution[k] = processes[k][0]
        ind = 0
        for j in range(0, n):
            if execution[j] != 0 and i >= arrivalArray[j]:
                execution[j] = execution[j] - 1
                Result.append(j + 1)
                ind = 1
                break
        if ind == 0:
            Result.append(-1)
    print("Timeline length: ", LCM)
    for i in range(0, LCM):
        startingPoints.append(i)
        if Result[i] != - 1:
            print("From% d to% d: p% d " % (i, i + 1, Result[i]), file=logFile)

            tasksArray.append(Result[i])
        else:
            print(" From% d to% d: Empty slot " % (i, i + 1) , file=logFile)
            tasksArray.append(0)

    startingPoints.append(i + 1)
    resultArray.append(startingPoints)
    resultArray.append(tasksArray)
    return resultArray

def rateMonotonicScheduling(processes):
    logFile = open("log/RMS.log", "w+")
    print("RATE MONOTONIC SCHEDULING: START\n", file=logFile)
    print("Rate Monotonic Scheduling:")
    finalArray = []
    n = len(processes)
    processes.sort(key=lambda x: x[0])
    print(processes, file=logFile)
    print(processes)
    u = 0
    for j in range(0, n):
        u = u + processes[j][0] / float(processes[j][1])
    print("Utilization:% f" % (u), file=logFile)
    print("Utilization:% f" % (u))
    if u <= 1:
        Ub = n * (pow(2, 1 / float(n)) - 1)
        if u <= Ub:
            print("processes are schedulable", file=logFile)
            print("processes are schedulable")
            finalArray = printSequence(processes, n, logFile)
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
                    print("Processes are not schedulable since processes% d can't meet deadline" % (ind1), file=logFile)
                    print("Processes are not schedulable since processes% d can't meet deadline" % (ind1))
                    print("\n")
                    success = 0
                    break
            if success == 1:
                print("processes are schedulable", file=logFile)
                print("Processes are schedulable")
                finalArray = printSequence(processes, n, logFile)
    else:
        print("processes are not schedulable", file=logFile)
        print("Processes are not schedulable")
    print("RATE MONOTONIC SCHEDULING: ENDn\n\n\n", file=logFile)
    print("\n-------------------------------------------------\n")
    return finalArray
