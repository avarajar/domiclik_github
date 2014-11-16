from django.contrib import admin
from .models import *
from .views import *

#class TituloAdicionaleInline(admin.TabularInline):
#	model = TituloAdicionale

class RestaurantAdmin(admin.ModelAdmin):
	list_filter = ('ciudad',)

class TituloA_admin(admin.ModelAdmin):
	list_display = ('titulo','menuesp')
	list_filter = ('restaurant',)
	#raw_id_fields=('temporada',) 
	#extra=1

	#def formfield_for_foreignkey(self, db_field, request, **kwargs):
	#	if db_field.name == 'restaurant':
	#		urlactual=request.get_full_path()
	#		urlactual=urlactual.split('/')
	#		_idrest=int(urlactual[4])
	#		kwargs["queryset"] = Restaurante.objects.filter(id=_idrest)
	#	return super(TituloA_admin, self).formfield_for_foreignkey(db_field, request, **kwargs)
class TituloADos_admin(admin.ModelAdmin):
	list_display = ('titulo','menuesp')
	list_filter = ('restaurant',)

class TituloATres_admin(admin.ModelAdmin):
	list_display = ('titulo','menuesp')
	list_filter = ('restaurant',)


class MenuEspecifico(admin.ModelAdmin):
	list_display = ('id','titulo','categoria','restaurant')
	list_filter = ('restaurant__nombre','categoria')

class Categoria_Admin(admin.ModelAdmin):
	list_filter = ('restaurant',)

class AdiUnicoAdmin (admin.ModelAdmin):
	list_display =('nombre','menuesp')
	list_filter = ('restaurant',)

class AdiUnicoDosAdmin (admin.ModelAdmin):
	list_display =('nombre','menuesp')
	list_filter = ('restaurant',)

class AdiUnicoTresAdmin (admin.ModelAdmin):
	list_display =('nombre','menuesp')
	list_filter = ('restaurant',)


class AdicionalAdmin (admin.ModelAdmin):
	list_display =('nombre','menuesp')
	list_filter = ('restaurant',)

class AdicionalDosAdmin (admin.ModelAdmin):
	list_display =('nombre','menuesp')
	list_filter = ('restaurant',)

class AdicionalTresAdmin (admin.ModelAdmin):
	list_display =('nombre','menuesp')
	list_filter = ('restaurant',)

class PedidoAdmin (admin.ModelAdmin):
	list_display =('fecha','codigo','restaurant','ciudad','nombre','correo','telefono','direccion','pedido_total')
	list_filter = ('restaurant','codigo',)

	def pedido_total(self,obj):
	 	return u'%s' % obj.pedido_completo
	pedido_total.allow_tags=True

admin.site.register(Ciudade)
admin.site.register(Sectore)
admin.site.register(Tipo)
admin.site.register(Restaurante, RestaurantAdmin)
admin.site.register(Categoria, Categoria_Admin)
admin.site.register(Menuesp,MenuEspecifico )
admin.site.register(TituloAdicionale, TituloA_admin)
admin.site.register(TituloAdicionalDos, TituloADos_admin)
admin.site.register(TituloAdicionalTres, TituloATres_admin)
admin.site.register(AdiUnico, AdiUnicoAdmin)
admin.site.register(AdiUnicoDos, AdiUnicoDosAdmin)
admin.site.register(AdiUnicoTres, AdiUnicoTresAdmin)
admin.site.register(Adicionale, AdicionalAdmin)
admin.site.register(AdicionalDos, AdicionalDosAdmin)
admin.site.register(AdicionalTres, AdicionalTresAdmin)
admin.site.register(Pedido, PedidoAdmin)

