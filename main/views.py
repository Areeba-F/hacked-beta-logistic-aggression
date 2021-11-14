from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from numpy import greater


# Create your views here.
def say_hello(request):

    return render(request, 'hello.html')

def cardio_test(request): 
    name = request.POST['your_name']
    results = MLEngine(request) 
    if (results == True):
        return render(request, 'positive.html')
    else:
        return render(request, 'negative.html', {'name': name })

def MLEngine(request):
    import pandas as pandas
    import numpy as numpy
    import matplotlib.pyplot as plot
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression    
    from sklearn.metrics import accuracy_score
    ## initialize variables from form
    age = int(request.POST['your_age'])
    age = age * 365
    height = int(request.POST['your_height'])
    weight = int(request.POST['your_weight'])
    sbp = int(request.POST['your_sbp'])
    dbp = int(request.POST['your_dbp'])

    ## intialize variables from radio buttons
    gender = request.POST['gender']
    if(gender == 'Male'):
        gender = 2
    else:
        gender = 1

    cholestoral = request.POST['cholestoral']

    if(cholestoral == 'norm'):
        cholestoral = 1
    elif(cholestoral == 'abvnorm'):
        cholestoral = 2
    else:
        cholestoral = 3

    glucose = request.POST['cholestoral']
    if(glucose == 'norm'):
        glucose = 1
    elif(glucose == 'abvnorm'):
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
         
    print(age, gender, height, weight, sbp, dbp, cholestoral, glucose, smoke, drink, exercise)



    Data = pandas.read_csv('Rcardiotrain.csv')
    x = Data.iloc[:, :-1]
    y = Data.iloc[:, -1]

    x_training, x_testing, y_training, y_testing = train_test_split(x, y, test_size = 0.20, random_state = 42)

    scaler = StandardScaler()
    x_training = scaler.fit_transform(x_training)
    x_testing = scaler.transform(x_testing)

    model = LogisticRegression()
    model.fit(x_training, y_training) # we fit/train/teach the model with our training data
    predicted_results = model.predict(x_testing)

    accuracy_score(y_testing, predicted_results)

    result = model.predict(scaler.transform([[age, gender, height, weight, sbp, dbp, cholestoral, glucose, smoke, drink, exercise]]))
    print(result)
    if result == 0:
        return False
    elif result ==1:
        return True
