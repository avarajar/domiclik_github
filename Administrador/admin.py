from django.contrib import admin
from .models import *

#class TituloAdicionaleInline(admin.TabularInline):
#	model = TituloAdicionale


class TituloA_admin(admin.ModelAdmin):
	list_display = ('titulo',)
	#raw_id_fields=('temporada',) 
	#extra=1

	#def formfield_for_foreignkey(self, db_field, request, **kwargs):
	#	if db_field.name == 'restaurant':
	#		urlactual=request.get_full_path()
	#		urlactual=urlactual.split('/')
	#		_idrest=int(urlactual[4])
	#		kwargs["queryset"] = Restaurante.objects.filter(id=_idrest)
	#	return super(TituloA_admin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class MenuEspecifico(admin.ModelAdmin):
	list_display = ('id','titulo','categoria','restaurant')
	list_filter = ('restaurant__nombre','categoria')

admin.site.register(Ciudade)
admin.site.register(Sectore)
admin.site.register(Tipo)
admin.site.register(Restaurante)
admin.site.register(Categoria)
admin.site.register(Menuesp,MenuEspecifico )
admin.site.register(TituloAdicionale, TituloA_admin)
admin.site.register(AdiUnico)
admin.site.register(Adicionale)