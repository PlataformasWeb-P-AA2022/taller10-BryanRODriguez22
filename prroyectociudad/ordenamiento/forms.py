from django.forms import ModelForm
from django import forms

from ordenamiento.models import *

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'parroquia_tipo'] 

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia'] 