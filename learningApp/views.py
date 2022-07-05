from django.shortcuts import render, redirect
from django.http import HttpResponse
from learningApp.forms import CarroForm
from learningApp.models import Carro
# Create your views here.


def helloWorld(request):

    return HttpResponse('Hello World in Python and Django')


def home(request):
    # dicionário de teste
    dates = {}
    dates['db_id'] = Carro.objects.all()

    return render(request, 'index.html', dates)


def form(request):
    data = {}
    data['form_id'] = CarroForm()

    return render(request, 'form.html', data)


def create(request):
    # Recebe os dados do formulário, salva os dados e redireciona para a home (inicio)
    form = CarroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('inicio')


def view(request, pk):
    dados = {}
    dados['db_id'] = Carro.objects.get(pk=pk)

    return render(request, 'view.html', dados)
