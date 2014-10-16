from django.db import models

class Ciudade(models.Model):
	nombre = models.CharField(max_length=60)
	
	def __str__(self):
		return self.nombre

class Sectore(models.Model):
	nombre = models.CharField(max_length=60)
	

	def __str__(self):
		return self.nombre

class Tipo(models.Model):
	nombre = models.CharField(max_length=60)
	

	def __str__(self):
		return self.nombre

class Restaurante(models.Model):
	nombre = models.CharField(max_length=60)
	descripcion = models.TextField(blank = True, default="descripcion")
	logo = models.ImageField(upload_to = "logos")
	ciudad = models.ForeignKey(Ciudade)
	sector = models.ForeignKey(Sectore)
	tipo = models.ForeignKey(Tipo)
	hora_abrir = models.TimeField("%H")
	hora_cerrar = models.TimeField("%H")
	precio_domicilio = models.IntegerField()

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	titulo = models.CharField(max_length=60)
	imagen_categoria = models.ImageField(upload_to = "categorias")
	restaurant = models.ForeignKey(Restaurante)

	
	def __str__(self):
		return self.titulo

class Menuesp(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	precio = models.IntegerField()
	ciudad = models.ForeignKey(Ciudade)
	sector = models.ForeignKey(Sectore)
	tipo = models.ForeignKey(Tipo)
	restaurant = models.ForeignKey(Restaurante)
	categoria = models.ForeignKey(Categoria)

	
	def __str__(self):
		return self.titulo


class TituloAdicionale(models.Model):
	titulo = models.CharField(max_length=60,blank=True)
	menuesp = models.ForeignKey(Menuesp)
	
	def __str__(self):
		return self.titulo

class AdiUnico(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	menuesp = models.ForeignKey(Menuesp)
	
	def __str__(self):
		return self.nombre

class Adicionale(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	precio = models.IntegerField()
	menuesp = models.ForeignKey(Menuesp)
	
	def __str__(self):
		return self.nombre






