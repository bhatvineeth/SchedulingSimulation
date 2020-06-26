import io
import sys

from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect
from .forms import UserCreationForm
from Main import edf, rms, fcfs, sjf

@csrf_protect
def openSimulator(request) :
    # for printing the console into a variable
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    if request.method == 'POST':
        form = UserCreationForm()
        final_array = request.POST.get('final_array')
        interval = request.POST.get('interval')
        noOfTasks = request.POST.get('noOfTasks')
        #form['interval'].initial = interval

        # splitting the input into desired format
        algorithmInputArray = arraySplit(final_array)
        # calculating rate monotonic scheduling algorithm
        rmsInputArray = rmsInputArrayCreator(algorithmInputArray)
        rmsArray = rms.rateMonotonicScheduling(rmsInputArray)

        # calculate earliest deadline first scheduling algorithm
        edfArray = edf.earliestDeadlineFirstAlgorithm(algorithmInputArray)

        # calculate first come first serve scheduling algorithm
        fcfsInputArray = fcfsInputArrayCreator(algorithmInputArray)
        fcfsArray = fcfs.firstComeFirstServe(fcfsInputArray)

        # calculate shortest job first scheduling algorithm
        sjfInputArray = fcfsInputArrayCreator(algorithmInputArray)
        sjfArray = sjf.shortestJobFirst(sjfInputArray)

        # formating the input array to send it back to screen
        algorithmInputArray = returnInputArray(algorithmInputArray)

        # writing standard output to variable
        outputConsole = new_stdout.getvalue()
        sys.stdout = old_stdout  # setting the standard output back to console

        return render(request, 'index.html',{'sjfArray': sjfArray, 'fcfsArray': fcfsArray, 'edfArray': edfArray, 'rmsArray': rmsArray, 'noOfTasks': noOfTasks,'algorithmInputArray': algorithmInputArray, 'form': form, 'outputConsole': outputConsole})
    else:
        form = UserCreationForm()
        outputConsole = new_stdout.getvalue()
        sys.stdout = old_stdout  # setting the standard output back to console
        return render(request, 'index.html', {'sjfArray': [], 'fcfsArray': [], 'edfArray': [], 'rmsArray': [], 'noOfTasks': [],'algorithmInputArray': [], 'form': form, 'outputConsole': outputConsole})


def arraySplit(algorithmInputs):
    algorithmInputs = algorithmInputs[:-1]
    algorithmInputs = algorithmInputs.split("|")
    algorithmInputArray = []
    for algorithmInput in algorithmInputs:
        algorithmInput = algorithmInput[:-1]
        algorithmInputArray.append(list(map(int, algorithmInput.split(",", -1))))
    return algorithmInputArray

def rmsInputArrayCreator(algorithmInputs):
    rmsInputArray = []
    for algorithmInput in algorithmInputs:
        taskArray = []
        taskArray.append(algorithmInput[1])
        taskArray.append(algorithmInput[2])
        taskArray.append(algorithmInput[4])
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

def returnInputArray(algorithmInputArray):
    algorithmInputArray.sort(key=lambda x: x[1])
    for inputArray in algorithmInputArray:
        inputArray[1:]
    return algorithmInputArray