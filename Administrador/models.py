#encoding:utf-8
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
#from slughifi import slughifi
from smart_selects.db_fields import ChainedForeignKey

class Ciudade(models.Model):
	nombre = models.CharField(max_length=60)
	slug = models.SlugField(max_length=250, blank=True, default='')

	
	
	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nombre)
		super(Ciudade, self).save(*args, **kwargs)
	

class Sectore(models.Model):
	nombre = models.CharField(max_length=60)
	ciudad = models.ForeignKey(Ciudade)
	slug_sector = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.slug_sector:
			self.slug_sector = slugify(self.nombre)
		super(Sectore, self).save(*args, **kwargs)

class Tipo(models.Model):
	nombre = models.CharField(max_length=60)
	slug_tipo = models.SlugField(max_length=250, blank=True, default='')
	

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.slug_tipo:
			self.slug_tipo = slugify(self.nombre)
		super(Tipo, self).save(*args, **kwargs)

class Restaurante(models.Model):
	nombre = models.CharField(max_length=60)
	descripcion = models.TextField(blank = True, default="descripcion")
	logo = models.ImageField(upload_to = "logos")
	ciudad = models.ForeignKey(Ciudade)
	sector = models.ManyToManyField(Sectore)
	tipo = models.ManyToManyField(Tipo)
	hora_abrir = models.TimeField()
	hora_cerrar = models.TimeField()
	precio_domicilio = models.IntegerField()
	entrega = models.CharField(max_length=60)
	slug_restaurant = models.SlugField(max_length=250, blank=True, default='')

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.slug_restaurant:
			self.slug_restaurant = slugify(self.nombre)
		super(Restaurante, self).save(*args, **kwargs)

class Categoria(models.Model):
	titulo = models.CharField(max_length=60)
	imagen_categoria = models.ImageField(upload_to = "categorias")
	restaurant = models.ForeignKey(Restaurante)
	promocion = models.BooleanField()

	
	def __unicode__(self):
		return self.titulo

class Menuesp(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField(blank = True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	
	
	categoria = ChainedForeignKey(
		Categoria,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)

	
	def __unicode__(self):
		return self.titulo

	


class TituloAdicionale(models.Model):
	titulo = models.CharField(max_length=60,blank=True)
	restaurant = models.ForeignKey(Restaurante)
	

	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field= "restaurant",
		chained_model_field= "restaurant",
		show_all=False,
		auto_choose=True
		)

	
	def __unicode__(self):
		return self.titulo

class TituloAdicionalDos(models.Model):
	titulo = models.CharField(max_length=60,blank=True)
	restaurant = models.ForeignKey(Restaurante)
	

	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field= "restaurant",
		chained_model_field= "restaurant",
		show_all=False,
		auto_choose=True
		)

	
	def __unicode__(self):
		return self.titulo

class TituloAdicionalTres(models.Model):
	titulo = models.CharField(max_length=60,blank=True)
	restaurant = models.ForeignKey(Restaurante)
	

	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field= "restaurant",
		chained_model_field= "restaurant",
		show_all=False,
		auto_choose=True
		)

	
	def __unicode__(self):
		return self.titulo

class AdiUnico(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	
	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)
	
	titulo =ChainedForeignKey(
		TituloAdicionale,
		chained_field="menuesp",
		chained_model_field="menuesp",
		show_all=False,
		auto_choose=True
		)
	
	def __unicode__(self):
		return self.nombre

class AdiUnicoDos(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	
	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)
	
	titulo =ChainedForeignKey(
		TituloAdicionalDos,
		chained_field="menuesp",
		chained_model_field="menuesp",
		show_all=False,
		auto_choose=True
		)
	
	def __unicode__(self):
		return self.nombre

class AdiUnicoTres(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	
	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)
	
	titulo = ChainedForeignKey(
		TituloAdicionalTres,
		chained_field="menuesp",
		chained_model_field="menuesp",
		show_all=False,
		auto_choose=True
		)
	
	def __unicode__(self):
		return self.nombre

class Adicionale(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)
	titulo =ChainedForeignKey(
		TituloAdicionale,
		chained_field="menuesp",
		chained_model_field="menuesp",
		show_all=False,
		auto_choose=True
		)
	
	def __unicode__(self):
		return self.nombre

class AdicionalDos(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)
	titulo =ChainedForeignKey(
		TituloAdicionalDos,
		chained_field="menuesp",
		chained_model_field="menuesp",
		show_all=False,
		auto_choose=True
		)
	
	def __unicode__(self):
		return self.nombre

class AdicionalTres(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	restaurant = models.ForeignKey(Restaurante)
	menuesp = ChainedForeignKey(
		Menuesp,
		chained_field="restaurant",
		chained_model_field="restaurant",
		show_all=False,
		auto_choose=True
		)
	titulo =ChainedForeignKey(
		TituloAdicionalTres,
		chained_field="menuesp",
		chained_model_field="menuesp",
		show_all=False,
		auto_choose=True
		)
	
	def __unicode__(self):
		return self.nombre

class Pedido(models.Model):
	codigo = models.CharField(max_length=60)
	nombre = models.CharField(max_length=60)
	correo = models.EmailField(max_length=75)
	telefono = models.CharField(max_length=60)
	barrio = models.CharField(max_length=60)
	direccion = models.TextField()
	restaurant =models.CharField(max_length=60)
	pedido_completo = models.TextField()
	# costo = models.IntegerField()

	def __unicode__(self):
		return self.nombre

