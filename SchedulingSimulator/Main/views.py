import io
import sys

from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect
from .forms import UserCreationForm
from Main import schedulingAlgorithm

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
        rmsArray, edfArray, fcfsArray, sjfArray, rrArray = schedulingAlgorithm.schedule(algorithmInputArray)
        # formating the input array to send it back to screen
        algorithmInputArray = returnInputArray(algorithmInputArray)

        # writing standard output to variable
        outputConsole = new_stdout.getvalue()
        sys.stdout = old_stdout  # setting the standard output back to console

        return render(request, 'index.html', {'rrArray': rrArray, 'sjfArray': sjfArray, 'fcfsArray': fcfsArray, 'edfArray': edfArray, 'rmsArray': rmsArray, 'noOfTasks': noOfTasks,'algorithmInputArray': algorithmInputArray, 'form': form, 'outputConsole': outputConsole})
    else:
        form = UserCreationForm()
        outputConsole = new_stdout.getvalue()
        sys.stdout = old_stdout  # setting the standard output back to console
        return render(request, 'index.html', {'rrArray': [], 'sjfArray': [], 'fcfsArray': [], 'edfArray': [], 'rmsArray': [], 'noOfTasks': [],'algorithmInputArray': [], 'form': form, 'outputConsole': outputConsole})


def arraySplit(algorithmInputs):
    algorithmInputs = algorithmInputs[:-1]
    algorithmInputs = algorithmInputs.split("|")
    algorithmInputArray = []
    for algorithmInput in algorithmInputs:
        algorithmInput = algorithmInput[:-1]
        algorithmInputArray.append(list(map(int, algorithmInput.split(",", -1))))
    return algorithmInputArray

def returnInputArray(algorithmInputArray):
    algorithmInputArray.sort(key=lambda x: x[1])
    for inputArray in algorithmInputArray:
        inputArray[1:]
    return algorithmInputArray