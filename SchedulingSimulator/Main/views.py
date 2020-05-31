from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect
from .forms import UserCreationForm
from Main import edf, rms


from django.template import RequestContext

@csrf_protect
def openSimulator(request) :
    if request.method == 'POST':
        form = UserCreationForm()
        final_array = request.POST.get('final_array')
        interval = request.POST.get('interval')
        noOfTasks = request.POST.get('noOfTasks')
        form['interval'].initial = interval
        algorithmInputArray = arraySplit(final_array)
        edfArray = edf.earliestDeadlineFirstAlgorithm(algorithmInputArray)
        rmsInputArray = rmsInputArrayCreator(algorithmInputArray)
        rmsArray = rms.rateMonotonicScheduling(rmsInputArray)
        algorithmInputArray = returnInputArray(algorithmInputArray)
        return render(request, 'index.html',{'edfArray': edfArray, 'rmsArray': rmsArray, 'interval': interval, 'noOfTasks': noOfTasks,'algorithmInputArray': algorithmInputArray, 'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'index.html', {'edfArray': [], 'rmsArray': [], 'interval': [], 'noOfTasks': [],'algorithmInputArray': [], 'form': form})



# Create your views here.
def submitData(request):
    print("adasdadad")
    return render(request, 'index.html', {})

def inputPage(request):
    form = UserCreationForm()
    return render(request, 'input.html', {'form': form})

def openIndex(request):
    return render(request, 'index.html', {})

@csrf_protect
def submitInput(request):
    final_array = request.POST.get('final_array')
    interval = request.POST.get('interval')
    noOfTasks = request.POST.get('noOfTasks')
    algorithmInputArray = arraySplit(final_array)
    edfArray = edf.earliestDeadlineFirstAlgorithm(algorithmInputArray)
    rmsInputArray = rmsInputArrayCreator(algorithmInputArray)
    rmsArray = rms.rateMonotonicScheduling(rmsInputArray)
    algorithmInputArray = returnInputArray(algorithmInputArray)
    return render(request, 'index.html', {'edfArray': edfArray, 'rmsArray': rmsArray, 'interval': interval, 'noOfTasks': noOfTasks, 'algorithmInputArray': algorithmInputArray})

# TODO: Stay on same page when form submits
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['your_name']
            print(name)
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCreationForm()

    return render(request, 'name.html', {'form': form})

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
        rmsInputArray.append(taskArray)
    return  rmsInputArray

def returnInputArray(algorithmInputArray):
    algorithmInputArray.sort(key=lambda x: x[2])
    for inputArray in algorithmInputArray:
        inputArray[1:]
    return algorithmInputArray