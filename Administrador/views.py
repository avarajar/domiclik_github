from .models import *
from time import  time
from datetime import  datetime
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.core import serializers
from django.utils import simplejson
from django.utils import timezone

def home(request):
	
	ciudades = Ciudade.objects.all()
	sectores = Sectore.objects.all()
	tipos = Tipo.objects.all()
	

	return render(request,"index.html",{"ciudades": ciudades, "sectores":sectores,"tipos":tipos,})

def restaurantes_ciudad(request,idc):
	
	ciudad = get_object_or_404(Ciudade, pk = idc)
	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.filter(ciudad_id = idc, )
	tipos = Tipo.objects.all()
	
	ahora = datetime.now().strftime("%H:%M:%S")
	

	

	return render(request,"index2.html",{
		"ciudades": ciudades,
		"restaurantes": restaurantes,
		"idcs" : idc,
		"ciudad": ciudad,
		"tipos": tipos,
		"ahora": ahora,})

def restaurantes_ciudad_sector(request,idc, idp):

	ciudad = get_object_or_404(Ciudade, pk = idc)
	sector = get_object_or_404(Sectore, pk = idp)
	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.filter(ciudad_id = idc, sector_id=idp)

	tipos = Tipo.objects.all()
	ahora = datetime.now().strftime("%H:%M:%S")
	

	

	return render(request,"index2.html",{
		"ciudad": ciudad,
		"sector": sector,
		"restaurantes": restaurantes,
		"idcs" : idc,
		
		"tipos": tipos,
		"ahora": ahora,})

def restaurantes_ciudad_sector_tipo(request,idc, idp, idk):

	ciudad = get_object_or_404(Ciudade, pk = idc)
	sector = get_object_or_404(Sectore, pk = idp)
	tipo = get_object_or_404(Tipo, pk = idk)
	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.filter(ciudad_id = idc, sector_id=idp, tipo_id=idk)

	tipos = Tipo.objects.all()
	ahora = datetime.now().strftime("%H:%M:%S")
	

	

	return render(request,"index2.html",{
		"ciudad": ciudad,
		"sector": sector,
		"tipo": tipo,
		"restaurantes": restaurantes,
		"idcs" : idc,
		
		"tipos": tipos,
		"ahora": ahora,})


def restaurantes(request):
	
	
	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.all()
	tipos = Tipo.objects.all()
	ahora = datetime.now().strftime("%H:%M:%S")
	

	

	return render(request,"index2.html",{
		"ciudades": ciudades,
		"restaurantes": restaurantes,
		"tipos": tipos,
		"ahora": ahora,})

	
def menu(request,idc):

	
	restaurant = get_object_or_404(Restaurante, pk = idc)
	restaurantes = Ciudade.objects.all()
	categoria = Categoria.objects.filter(restaurant_id=idc,)

	#menu = Menu.objects.filter(restaurant_id = idc,)
	menus = Menuesp.objects.filter(restaurant_id=idc,)
	

	

	return render(request,"index3.html",{
		"restaurant": restaurant,
		"categoria": categoria,
		"menus": menus,})

class Ajax(ListView):

	def get(self, request, *args, **kwargs):
		id_menu = request.GET['id']
		#id_rest = request.GET['idc']
		menuesp = Menuesp.objects.filter(pk=id_menu)
		adicionales = Adicionale.objects.filter(menuesp__id=id_menu)

		data1 = serializers.serialize('json', adicionales,
									fields=('nombre','precio',))
		data_a = simplejson.loads( data1 )

		data2 = serializers.serialize('json', menuesp,
									fields=('titulo','precio',))
		data_b = simplejson.loads( data2 )

		data=simplejson.dumps( {'data1':data_a, 'data2':data_b } )
		
		

	

		return HttpResponse(data, mimetype='application/json')


