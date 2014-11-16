#encoding:utf-8
from .models import *
from time import  time, localtime
from datetime import  datetime, time, timedelta
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, TemplateView, FormView
from django.core import serializers
from django.utils import simplejson
from django.utils import timezone
from django.utils.timezone import utc
from .forms import PedidoForm
import random
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives, EmailMessage

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
	restaurantes = Restaurante.objects.filter(ciudad__slug = slug, sector__slug_sector=slug_sector).order_by('nombre')

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
	restaurantes = Restaurante.objects.filter(ciudad__slug = slug, sector__slug_sector=slug_sector, tipo__slug_tipo=slug_tipo).order_by('nombre')

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
	now = datetime.now()

	# entero = int(now)
	hora= now.hour
	minutos = now.minute

	

	return render(request,"index2.html",{
		"ciudades": ciudades,
		"restaurantes": restaurantes,
		"tipos": tipos,
		"hora": hora,
		"minutos": minutos,})

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

	if request.method == 'POST': # If the form has been submitted...
		form = PedidoForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			logo = '<img src="http://domiclik.herokuapp.com/media/img/correos.png" height="170" width="500" alt=""><br>'
			nombre = form.cleaned_data['nombre']
			nombre_correo ='<strong>Cliente: </strong>'+nombre+'<br>'
			correo = form.cleaned_data['correo']
			correo_correo ='<strong>Correo:</strong>'+correo+'<br>'
			telefono = form.cleaned_data['telefono']
			telefono_correo ='<strong>Telefono: </strong>'+telefono+'<br>'
			barrio = form.cleaned_data['barrio']
			barrio_correo ='<strong>Barrio: </strong>'+barrio+'<br>'
			direccion = form.cleaned_data['direccion']
			direccion_correo ='<strong>Direccion: </strong>'+direccion+'<br>'
			ciudad = form.cleaned_data['ciudad']
			ciudad_correo = '<strong>Ciudad: </strong>'+ciudad+'<br>'
			restaurant = form.cleaned_data['restaurant']
			restaurant_correo ='<strong>Restaurante: </strong>'+restaurant+'<br>'
			chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
			id_pedido = ''.join(random.sample(chars, 8))
			id_pedido_correo ='<strong>Codigo de pedido: </strong>'+id_pedido+'<br>'
			pedido_completo = form.cleaned_data['pedido_completo']
			mensaje= '\n'.join([logo,nombre_correo, telefono_correo, barrio_correo,direccion_correo,ciudad_correo,restaurant_correo,id_pedido_correo,pedido_completo])
			recipients = ['domiclik.com@gmail.com','servicioalcliente.domiclik@hotmail.com','avarajame@gmail.com']
			recipients.append(correo)
			mail = EmailMessage('Nuevo Pedido: Domiclik', mensaje, 'ventas@domiclik.com', recipients,)
			mail.content_subtype="html"
			mail.send()
			fecha = datetime.now()
			pedido = Pedido()
			pedido.codigo = id_pedido
			pedido.nombre = nombre
			pedido.correo = correo
			pedido.telefono = telefono
			pedido.barrio = barrio
			pedido.direccion = direccion
			pedido.pedido_completo =pedido_completo
			pedido.restaurant =restaurant
			pedido.ciudad = ciudad
			pedido.fecha = fecha
			pedido.save()
                # Proce data in form.cleaned_data
                # ...
                return HttpResponseRedirect('/pedido') # Redirect after POST
        else:

        	form = PedidoForm() # An unbound form


	

	return render(request,"index3.html",{
		"restaurant": restaurant,
		"categoria": categoria,
		#"categoria_titulo": categoria_titulo,
		"menus": menus,
		"form": form,
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

	if request.method == 'POST': # If the form has been submitted...
		form = PedidoForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
		    logo = '<img src="http://domiclik.herokuapp.com/media/img/correos.png" height="170" width="500" alt=""><br>'
		    nombre = form.cleaned_data['nombre']
		    nombre_correo ='<strong>Cliente: </strong>'+nombre+'<br>'
		    correo = form.cleaned_data['correo']
		    correo_correo ='<strong>Correo: </strong>'+correo+'<br>'
		    telefono = form.cleaned_data['telefono']
		    telefono_correo ='<strong>Telefono: </strong>'+telefono+'<br>'
		    barrio = form.cleaned_data['barrio']
		    barrio_correo ='<strong>Barrio: </strong>'+barrio+'<br>'
		    direccion = form.cleaned_data['direccion']
		    direccion_correo ='<strong>Direccion: </strong>'+direccion+'<br>'
		    ciudad = form.cleaned_data['ciudad']
		    ciudad_correo = '<strong>Ciudad: </strong>'+ciudad+'<br>'
		    restaurant = form.cleaned_data['restaurant']
		    restaurant_correo ='<strong>Restaurante: </strong>'+restaurant+'<br>'
		    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		    id_pedido = ''.join(random.sample(chars, 8))
		    id_pedido_correo ='<strong>Codigo de pedido: </strong>'+id_pedido+'<br>'
		    pedido_completo = form.cleaned_data['pedido_completo']
		    mensaje= '\n'.join([logo,nombre_correo, telefono_correo, barrio_correo,direccion_correo,ciudad_correo,restaurant_correo,id_pedido_correo,pedido_completo])
		    recipients = ['domiclik.com@gmail.com','servicioalcliente.domiclik@hotmail.com','avarajame@gmail.com']
		    recipients.append(correo)
		    mail = EmailMessage('Nuevo Pedido: Domiclik', mensaje, 'ventas@domiclik.com', recipients,)
		    mail.content_subtype="html"
		    mail.send()
		    fecha = datetime.now()
		    pedido = Pedido()
		    pedido.codigo = id_pedido
		    pedido.nombre = nombre
		    pedido.correo = correo
		    pedido.telefono = telefono
		    pedido.barrio = barrio
		    pedido.direccion = direccion
		    pedido.pedido_completo =pedido_completo
		    pedido.restaurant =restaurant
		    pedido.ciudad = ciudad
		    pedido.fecha = fecha
		    pedido.save()
		    
                # Process the data in form.cleaned_data
                # ...
                return HttpResponseRedirect('/pedido') # Redirect after POST
        else:

        	form = PedidoForm() # An unbound form

	

	return render(request,"index3.html",{
		"restaurant": restaurant,
		"categoria": categoria,
		"form": form,
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


# class PedidoForm(FormView):
# 	template_name = 'index4.html'
# 	form_class = PedidoForm
# 	success_url = '/'

# 	def form_valid(self, form):
# 		self.object = form.save(commit = True)
# 		return super(PedidoForm, self).form_valid(form)

# def pedido_form(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = PedidoForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#         	form.save()
#                 # Process the data in form.cleaned_data
#                 # ...
#                 return HttpResponseRedirect('/pedido/') # Redirect after POST
#     else:
#         form = PedidoForm() # An unbound form

    
#     return render(request,"index4.html",{
# 		"form": form,
# 		})


def pedido(request):
	
	
	return render(request,"index4.html",{
		
		})

