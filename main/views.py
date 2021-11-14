from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from numpy import greater
from .forms import MedicalForm

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html')

def runtest(request): 
    ## initialize variables from form
    name = request.POST['your_name']
    age = request.POST['your_age']
    height = request.POST['your_height']
    weight = request.POST['your_weight']
    sbp = request.POST['your_sbp']
    dbp = request.POST['your_dbp']

    ## intialize variables from radio buttons
    gender = request.POST['gender']
    if(gender == 'Male'):
        gender = 2
    else:
        gender = 1

    cholestoral = request.POST['cholestoral']
    if(cholestoral == 'Normal'):
        cholestoral = 1
    elif(cholestoral == 'Above Normal'):
        cholestoral = 2
    else:
        cholestoral = 3

    glucose = request.POST['cholestoral']
    if(glucose == 'Normal'):
        glucose = 1
    elif(glucose == 'Above Normal'):
        glucose = 2
    else:
        glucose = 3

    smoke = request.POST['smoke']
    if(smoke == 'Yes'):
        smoke = 1
    else:
        smoke = 0

    drink = request.POST['drink']
    if(drink == 'Yes'):
        drink = 1
    else:    
        drink = 0

    exercise = request.POST['exercise']
    if(exercise == 'Yes'):
        exercise = 1
    else:
        exercise = 0


    ## get results from Machine Learning model
    ##result = predict(name, age, height, weight, sbp, dbp, gender, cholestoral, glucose, smoke, drink, exercise)

    results = False
    if (results == True):
        return render(request, 'positive.html')
    else:
        return render(request, 'negative.html', {'name': gender })

def test():
    return "test"


# need to clean age, no dayst