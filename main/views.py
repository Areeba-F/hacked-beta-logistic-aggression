from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x = 1
    return render(request, 'hello.html', {'name': x })


def runtest(request):
    return render(request, 'test.html', {'name': test()})

def test():
    return "test"


##