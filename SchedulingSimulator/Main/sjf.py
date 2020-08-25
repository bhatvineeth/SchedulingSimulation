def sjfScheduling(processesArray, executionTimeArray, periodArray, arrivalTimeArray, logFile) :
    exec_count = 0
    LCM = max((map(lambda x: x[1], processesArray)))
    while 1:
        ind = 0
        for j in range(0, len(processesArray)):
            if LCM % processesArray[j][1] == 0:
                ind = ind + 1
        if ind == len(processesArray):
            break
        else:
            LCM = LCM + 1
    print("Timeline length =", LCM)
    execArray = [99999] * len(executionTimeArray)
    resultStartingPoints = list(range(LCM + 1))
    resultArray = [0] * LCM
    for i in range(0, LCM):
        if i in arrivalTimeArray:
            arrivalTasksIndices = list(k for k, x in enumerate(arrivalTimeArray) if x == i);
            for q in arrivalTasksIndices:
                execArray[q] = executionTimeArray[q]
        if (exec_count == 0) :
            sjTask = execArray.index(min(execArray))
            if (99999 == min(execArray)) :
                continue;
            else:
                exec_count = min(execArray)
                arrivalTimeArray[sjTask] += periodArray[sjTask]
                execArray[sjTask] = 99999
        resultArray[i] = sjTask + 1
        exec_count -= 1
    sjfArray =[]
    sjfArray.append(resultStartingPoints)
    sjfArray.append(resultArray)
    print(sjfArray, file=logFile)
    return sjfArray

def schedule(processes) :
    logFile = open("log/SJF.log", "w+")
    print("Shortest Job First:")
    print(processes)
    executionTimeArray = []
    arrivalTimeArray = []
    periodArray = []
    processes.sort(key=lambda x: x[0])
    for process in processes:
        executionTimeArray.append(process[0])
        periodArray.append(process[1])
        arrivalTimeArray.append(process[2])
    resultArray = sjfScheduling(processes, executionTimeArray, periodArray, arrivalTimeArray, logFile)
    return resultArray
