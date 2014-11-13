
from django import forms
from django.forms import ModelForm
from .models import Pedido


class PedidoForm(forms.Form):
	# nombre_cliente = forms.CharField(max_length=60)
	# correo_cliente = forms.EmailField(max_length=75)
	# telefono_cliente = forms.CharField(max_length=60)
	# direccion = forms.CharField(max_length=160)
	nombre = forms.CharField(widget=forms.TextInput)
	correo = forms.CharField(widget=forms.EmailInput)
	telefono = forms.CharField(widget=forms.TextInput)

	barrio = forms.CharField(widget=forms.TextInput) 
	direccion = forms.CharField(widget=forms.Textarea)
	ciudad = forms.CharField(widget=forms.TextInput)
	restaurant =forms.CharField(widget=forms.TextInput)
	pedido_completo = forms.CharField(widget=forms.Textarea)
	# costo = forms.IntegerField(widget=forms.TextInput)


	class Meta:
	 	model = Pedido
	 	# fields = ('nombre', 'correo', 'telefono','direccion')

	def clean_nombre(self):
		diccionario_limpio = self.cleaned_data
		nombre = diccionario_limpio.get('nombre')
		if len(nombre) < 3:
			raise forms.ValidationError("El autor debe contener mas de tres caracteres")
		return nombre