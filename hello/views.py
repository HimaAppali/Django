from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Hello')

def hima(request):
    return HttpResponse('Hello Hima')

def bindu(request):
    return HttpResponse('Hello Bindu')

# dynamic name template syntax
# def somename(request, name):
#     return HttpResponse(f'Hello, {name.upper()}')

# Insted of retuting only a single string we can retrun a full html page or some python code ect
# insted of returing a single quote in default route i.e, index from above function
def index(request):
    return render(request, 'hello/index.html')

# Let's see rendering a page with some additional context like below
def somename(request, name):
    return render(request, 'hello/someone.html', {
        'name': name.upper()
    })
