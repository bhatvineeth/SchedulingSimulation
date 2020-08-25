import math


def rmsScheduling(processes, n, logFile):
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
                Result.append(processes[j][3])
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

def schedule(processes):
    logFile = open("log/RMS.log", "w+")
    print("RATE MONOTONIC SCHEDULING: START\n", file=logFile)
    print("Rate Monotonic Scheduling:")
    finalArray = []
    n = len(processes)
    processes.sort(key=lambda x: x[1])
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
            finalArray = rmsScheduling(processes, n, logFile)
        else:
            print("Processes are not schedulable since processes can't meet deadline" , file=logFile)
            print("Processes are not schedulable since processes can't meet deadline")
            print("\n")
    else:
        print("processes are not schedulable", file=logFile)
        print("Processes are not schedulable")
    print("RATE MONOTONIC SCHEDULING: ENDn\n\n\n", file=logFile)
    print("\n-------------------------------------------------\n")
    return finalArray
