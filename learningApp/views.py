from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def helloWorld(request):
    return HttpResponse('Hello World in Python and Django')


def home(request):
    # dicionário de teste
    data = {}
    data['carro'] = 'Gol'

    return render(request, 'index.html', data)


def form(request):

    return render(request, 'form.html')
