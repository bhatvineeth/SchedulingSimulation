from Main import rms, edf, fcfs, sjf


def schedule(algorithmInputArray):
    rmsInputArray = rmsInputArrayCreator(algorithmInputArray)
    rmsArray = rms.schedule(rmsInputArray)

    # calculate earliest deadline first scheduling algorithm
    edfArray = edf.schedule(algorithmInputArray)

    # calculate first come first serve scheduling algorithm
    fcfsInputArray = fcfsInputArrayCreator(algorithmInputArray)
    fcfsArray = fcfs.schedule(fcfsInputArray)

    # calculate shortest job first scheduling algorithm
    sjfInputArray = fcfsInputArrayCreator(algorithmInputArray)
    sjfArray = sjf.schedule(sjfInputArray)
    return rmsArray, edfArray, fcfsArray, sjfArray

def rmsInputArrayCreator(algorithmInputs):
    rmsInputArray = []
    algorithmInputs.sort(key=lambda x: x[1])
    i = 0
    for algorithmInput in algorithmInputs:
        taskArray = []
        taskArray.append(algorithmInput[1])
        taskArray.append(algorithmInput[2])
        taskArray.append(algorithmInput[4])
        i += 1
        taskArray.append(i)
        rmsInputArray.append(taskArray)
    return  rmsInputArray

def fcfsInputArrayCreator(algorithmInputs):
    fcfsInputArray = []
    for algorithmInput in algorithmInputs:
        taskArray = []
        taskArray.append(algorithmInput[1])
        taskArray.append(algorithmInput[2])
        taskArray.append(algorithmInput[4])
        fcfsInputArray.append(taskArray)
    return fcfsInputArray