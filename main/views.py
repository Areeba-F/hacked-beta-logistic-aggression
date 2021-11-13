from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x = 1
    return render(request, 'hello.html', {'name': x })


def runtest(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        from test.py import test
        testValue = test()
        return render(request, 'hello.html', {'name': testValue })

def test():
    return "test"