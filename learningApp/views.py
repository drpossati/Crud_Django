from django.shortcuts import render
from django.http import HttpResponse
from learningApp.forms import CarroForm
# Create your views here.


def helloWorld(request):

    return HttpResponse('Hello World in Python and Django')


def home(request):
    # dicionário de teste
    data = {}
    data['carro'] = 'Gol'

    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form_id'] = CarroForm()

    return render(request, 'form.html', data)
