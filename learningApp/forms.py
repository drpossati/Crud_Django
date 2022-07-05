from django.forms import ModelForm
from learningApp.models import Carro


# Create the form class
class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano']
