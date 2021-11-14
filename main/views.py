from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .forms import MedicalForm

# Create your views here.
def say_hello(request):
    forms = MedicalForm()
    x = 1
    return render(request, 'hello.html', {'name': x }, {'forms': forms})


def runtest(request): 
    name = myForm.cleaned_data['name']
    results = False
    if (results == True):
        return render(request, 'positive.html')
    else:
        return render(request, 'negative.html', {'name': name })

def test():
    return "test"


# need to clean age, no days