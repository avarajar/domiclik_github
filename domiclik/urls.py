from django.conf.urls import patterns, include, url
from Administrador.views import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Administrador.views.home', name='home'),
    #url(r'^$', Home.as_view(), name='home'),
    
    url(r'^restaurantes/$', 'Administrador.views.restaurantes', name='restaurantes'),
    url(r'^restaurantes/(?P<slug>[-\w]+)/$', 'Administrador.views.restaurantes_ciudad', name='restaurantes_ciudad'),
    url(r'^restaurantes/(?P<slug>[-\w]+)/(?P<slug_sector>[-\w]+)/$', 'Administrador.views.restaurantes_ciudad_sector', name='restaurantes_ciudad_sector'),
    url(r'^restaurantes/(?P<slug>[-\w]+)/(?P<slug_sector>[-\w]+)/(?P<slug_tipo>[-\w]+)$', 'Administrador.views.restaurantes_ciudad_sector_tipo', name='restaurantes_ciudad_sector_tipo'),
    url(r'^menu/(?P<slug_restaurant>[-\w]+)/(?P<slug>[-\w]+)/(?P<slug_sector>[-\w]+)/$', 'Administrador.views.menu_ciudad_sector', name='menu_ciudad_sector'),
    url(r'^menu/(?P<slug_restaurant>[-\w]+)/(?P<slug>[-\w]+)/(?P<slug_sector>[-\w]+)/(?P<slug_tipo>[-\w]+)$', 'Administrador.views.menu_ciudad_sector_tipo', name='menu_ciudad_sector_tipo'),
    url(r'^ajax/$', Ajax.as_view(), name='ajax'),
    url(r'^ajax_ciudad_sector/$', Ajax_Ciudad_Sector.as_view(), name='ajax_ciudad_sector'),
    url(r'^chaining/', include('smart_selects.urls')),
    #url(r'^restaurantes/menu/(\d+)$', 'Administrador.views.menu_esp', name='menu_esp'),
    #url(r'^restaurantes/(?P<pk>[\d]+)$', restaurantesdetail.as_view(), name='restaurantes'),

    # url(r'^domiclik/', include('domiclik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, } ),
)
