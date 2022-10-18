from django import forms
from django.forms import ModelForm
from .models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        
        fields = ('ID_empleado', 'Nombre', 'Tipo', 'Area', 'Spot', 'Supervisor', 'Correo','CorreoSupervisor')

        widgets = {
            'ID_empleado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID_empleado'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo'}),
            'Area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}),
            'Spot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spot'}),
            'Supervisor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
            'CorreoSupervisor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CorreoSupervisor'}),
        }