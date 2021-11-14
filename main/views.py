from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def say_hello(request):
    x = 1
    return render(request, 'hello.html', {'name': x })


def runtest(request): 
    results = False
    if (results == True):
        return render(request, 'positive.html')
    else:
        return render(request, 'negative.html')

def test():
    return "test"


# need to clean age, no days