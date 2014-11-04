from .models import *
from time import  time, localtime
from datetime import  datetime, time, timedelta
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, TemplateView
from django.core import serializers
from django.utils import simplejson
from django.utils import timezone
from django.utils.timezone import utc

def home(request):
	
	ciudades = Ciudade.objects.all().order_by('nombre')
	sectores = Sectore.objects.all().order_by('nombre')
	tipos = Tipo.objects.all().order_by('nombre')
	
	return render(request,"index.html",{"ciudades": ciudades, "sectores":sectores,"tipos":tipos,})

def restaurantes_ciudad(request,slug):
		


	
    
	ciudad = get_object_or_404(Ciudade,slug = slug)

	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.filter(ciudad__slug = slug )
	tipos = Tipo.objects.all()
	
	now = datetime.now()

	# entero = int(now)
	hora= now.hour
	minutos = now.minute
	

	

	return render(request,"index2.html",{
		"ciudades": ciudades,
		"restaurantes": restaurantes,
		# "idcs" : idc,
		"ciudad": ciudad,
		"tipos": tipos,
		"hora": hora,
		"minutos": minutos,})

def restaurantes_ciudad_sector(request,slug, slug_sector):

	ciudad = get_object_or_404(Ciudade, slug = slug)
	sector = get_object_or_404(Sectore, slug_sector = slug_sector)
	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.filter(ciudad__slug = slug, sector__slug_sector=slug_sector)

	tipos = Tipo.objects.all()
	now = datetime.now()

	# entero = int(now)
	hora= now.hour
	minutos = now.minute

	
	

	return render(request,"index2.html",{
		"ciudad": ciudad,
		"sector": sector,
		"restaurantes": restaurantes,
		# "idcs" : idc,
		
		"tipos": tipos,
		"hora": hora,
		"minutos": minutos,})


def restaurantes_ciudad_sector_tipo(request,slug, slug_sector, slug_tipo):

	ciudad = get_object_or_404(Ciudade, slug = slug)
	sector = get_object_or_404(Sectore, slug_sector = slug_sector)
	tipo = get_object_or_404(Tipo, slug_tipo = slug_tipo)
	ciudades = Ciudade.objects.all()
	restaurantes = Restaurante.objects.filter(ciudad__slug = slug, sector__slug_sector=slug_sector, tipo__slug_tipo=slug_tipo)

	tipos = Tipo.objects.all()
	now = datetime.now()

	# entero = int(now)
	hora= now.hour
	minutos = now.minute

	

	return render(request,"index2.html",{
		"ciudad": ciudad,
		"sector": sector,
		"tipo": tipo,
		"restaurantes": restaurantes,
		# "idcs" : idc,
		
		"tipos": tipos,
		"hora": hora,
		"minutos": minutos,})


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

def menu_ciudad_sector(request,slug_restaurant,slug,slug_sector):

	
	restaurant = get_object_or_404(Restaurante, slug_restaurant = slug_restaurant)
	ciudad = get_object_or_404(Ciudade, slug = slug)
	sector = get_object_or_404(Sectore, slug_sector = slug_sector)
	
	#categoria_titulo = get_object_or_404(Categoria, pk = idc)
	restaurantes = Ciudade.objects.all()
	categoria = Categoria.objects.filter(restaurant__slug_restaurant=slug_restaurant,).order_by('promocion')
	# tituloa = TituloAdicionale.objects.filter(menuesp_id=idc,)
	#menu = Menu.objects.filter(restaurant_id = idc,)
	
	menus = Menuesp.objects.filter(restaurant__slug_restaurant=slug_restaurant,restaurant__ciudad__slug =slug, restaurant__sector__slug_sector = slug_sector,)
	now = datetime.now()

	# entero = int(now)
	hora= now.hour
	minutos = now.minute


	

	return render(request,"index3.html",{
		"restaurant": restaurant,
		"categoria": categoria,
		#"categoria_titulo": categoria_titulo,
		"menus": menus,
		
		"ciudad": ciudad,
		"sector": sector,
		 # "tituloa": tituloa,
		
		"hora": hora,
		"minutos": minutos,})	


def menu_ciudad_sector_tipo(request,slug_restaurant,slug,slug_sector,slug_tipo):

	
	restaurant = get_object_or_404(Restaurante, slug_restaurant = slug_restaurant)
	ciudad = get_object_or_404(Ciudade, slug = slug)
	sector = get_object_or_404(Sectore, slug_sector = slug_sector)
	tipo = get_object_or_404(Tipo, slug_tipo = slug_tipo)
	#categoria_titulo = get_object_or_404(Categoria, pk = idc)
	restaurantes = Ciudade.objects.all()
	categoria = Categoria.objects.filter(restaurant__slug_restaurant=slug_restaurant,).order_by('promocion')
	# tituloa = TituloAdicionale.objects.filter(menuesp_id=idc,)
	#menu = Menu.objects.filter(restaurant_id = idc,)
	
	menus = Menuesp.objects.filter(restaurant__slug_restaurant=slug_restaurant,restaurant__ciudad__slug =slug, restaurant__sector__slug_sector = slug_sector, restaurant__tipo__slug_tipo = slug_tipo,)
	now = datetime.now()

	# entero = int(now)
	hora= now.hour
	minutos = now.minute


	

	return render(request,"index3.html",{
		"restaurant": restaurant,
		"categoria": categoria,
		#"categoria_titulo": categoria_titulo,
		"menus": menus,
		"tipo":tipo,
		"ciudad": ciudad,
		"sector": sector,
		# "tituloa": tituloa,
		"hora": hora,
		"minutos": minutos,})

class Ajax_Ciudad_Sector(TemplateView):
	def get(self, request, *args, **kwargs):
		id_ciudad = request.GET['ciudad']
		sector = Sectore.objects.filter(ciudad__slug=id_ciudad)
		data = serializers.serialize('json',sector,
									fields=('nombre','id','slug_sector',))
		#data_sector = simplejson.loads(data1)

		return HttpResponse(data,mimetype='application/json')


class Ajax(ListView):

	def get(self, request, *args, **kwargs):
		id_menu = request.GET['id']
		#id_rest = request.GET['idc']
		menuesp = Menuesp.objects.filter(pk=id_menu)
		titulo = TituloAdicionale.objects.filter(menuesp__id=id_menu)
		titulodos = TituloAdicionalDos.objects.filter(menuesp__id=id_menu)
		titulotres= TituloAdicionalTres.objects.filter(menuesp__id=id_menu)
		adicionales = Adicionale.objects.filter(menuesp__id=id_menu)
		adicionalesdos = AdicionalDos.objects.filter(menuesp__id=id_menu)
		adicionalestres = AdicionalTres.objects.filter(menuesp__id=id_menu)
		unicos = AdiUnico.objects.filter(menuesp__id=id_menu)
		unicosdos = AdiUnicoDos.objects.filter(menuesp__id=id_menu)
		unicostres = AdiUnicoTres.objects.filter(menuesp__id=id_menu)

		data1 = serializers.serialize('json', adicionales,
									fields=('nombre','precio', 'titulo',))
		data_a = simplejson.loads( data1 )

		data1a = serializers.serialize('json', adicionalesdos,
									fields=('nombre','precio', 'titulo',))
		data_a1 = simplejson.loads( data1a )

		data2a = serializers.serialize('json', adicionalestres,
									fields=('nombre','precio', 'titulo',))
		data_a2 = simplejson.loads( data2a )

		data2 = serializers.serialize('json', menuesp,
									fields=('titulo','precio',))
		data_b = simplejson.loads( data2 )

		data3 = serializers.serialize('json', titulo,
									fields=('titulo','id',))
		data_c = simplejson.loads( data3 )

		data3a = serializers.serialize('json', titulodos,
									fields=('titulo','id',))
		data_3a = simplejson.loads( data3a )

		data3b = serializers.serialize('json', titulotres,
									fields=('titulo','id',))
		data_3b = simplejson.loads( data3b )

		data4 = serializers.serialize('json', unicos,
									fields=('nombre','precio','titulo',))
		data_d = simplejson.loads( data4 )

		data4a = serializers.serialize('json', unicosdos,
									fields=('nombre','precio','titulo',))
		data_4a = simplejson.loads( data4a )

		data4b = serializers.serialize('json', unicostres,
									fields=('nombre','precio','titulo',))
		data_4b = simplejson.loads( data4b )


		data=simplejson.dumps( {'data1':data_a, 'data1a':data_a1, 'data1b':data_a2,
								 'data2':data_b, 'data3':data_c, 'data3a':data_3a,
								 'data3b':data_3b, 'data4':data_d, 
								 'data4a':data_4a,'data4b':data_4b,} )
		
		

	

		return HttpResponse(data, mimetype='application/json')


