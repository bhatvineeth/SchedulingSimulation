# Implementation of FCFS
# scheduling with different arrival time

# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0

    # calculating waiting time
    for i in range(1, n):

        # Add burst time of previous processes
        service_time[i] = (service_time[i - 1] +
                           bt[i - 1])

        # Find waiting time for current
        # process = sum - at[i]
        wt[i] = service_time[i] - at[i]

        # If waiting time for a process is in
        # negative that means it is already
        # in the ready queue before CPU becomes
        # idle so its waiting time is 0
        if (wt[i] < 0):
            wt[i] = 0


# Function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
    # Calculating turnaround time by
    # adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

    # Function to calculate average waiting


# and turn-around times.
def findavgTime(processes, n, bt, at):
    startingPoints = []
    endingPoints = []
    tasks = []
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time
    # of all processes
    findWaitingTime(processes, n, bt, wt, at)

    # Function to find turn around time for
    # all processes
    findTurnAroundTime(processes, n, bt, wt, tat)

    # Display processes along with all details
    #print("Processes   Burst Time   Arrival Time     Waiting",
    #      "Time   Turn-Around Time  Completion Time \n")
    total_wt = 0
    total_tat = 0
    lcm = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        if (lcm < compl_time):
            lcm = compl_time
        #print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],
        #     "\t\t", wt[i], "\t\t ", tat[i], "\t\t ", compl_time)
        #print("From ", at[i] + wt[i], "to ", compl_time, ": ", "Task ", i + 1)
        startingPoints.append(at[i] + wt[i])
        endingPoints.append(compl_time)
        tasks.append(i+1)

    print("Average waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = ", total_tat / n)


def fcfsScheduling(processesArray, executionTimeArray, periodArray, arrivalTimeArray, logFile) :

    exec_count = 0
    stack = []
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
    resultStartingPoints = list(range(LCM + 1))
    resultArray = [0] * LCM
    task = 0
    for i in range(0,LCM):
        if i in arrivalTimeArray:
            stack.extend(k for k, x in enumerate(arrivalTimeArray) if x == i)
        if exec_count == 0 and len(stack) != 0:
            task = stack[0]
            exec_count = executionTimeArray[task]
            period = periodArray[task]
            arrivalTimeArray[task] = arrivalTimeArray[task] + period
            resultArray[i] = task+1
            exec_count = exec_count - 1
        elif len(stack) != 0:
            resultArray[i] = task+1
            exec_count = exec_count - 1

        if exec_count == 0 and len(stack) != 0:
            stack.pop(0)
            task = 0
    fcfsArray =[]
    fcfsArray.append(resultStartingPoints)
    fcfsArray.append(resultArray)
    print(fcfsArray, file=logFile)
    return fcfsArray


def schedule(processes) :
    logFile = open("log/RMS.log", "w+")
    print("First Come First Serve:")
    print(processes)
    executionTimeArray = []
    arrivalTimeArray = []
    periodArray = []
    processes.sort(key=lambda x: x[0])
    for process in processes:
        executionTimeArray.append(process[0])
        periodArray.append(process[1])
        arrivalTimeArray.append(process[2])
    findavgTime(processes, len(processes), executionTimeArray, arrivalTimeArray)
    resultArray = fcfsScheduling(processes, executionTimeArray, periodArray, arrivalTimeArray, logFile)
    print("\n-------------------------------------------------\n")
    return resultArray





