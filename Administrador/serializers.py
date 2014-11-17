from rest_framework import serializers
from.models import *
from .models import Restaurante
from django.contrib.auth.models import User

class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model= Restaurante
		fields =('nombre','descripcion','logo','ciudad','sector','tipo','hora_abrir','hora_cerrar','precio_domicilio','entrega')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email')