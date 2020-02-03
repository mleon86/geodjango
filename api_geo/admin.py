from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Parada, Datos_Parada, Datos_Mapa

@admin.register(Parada)
class ParadaAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13

@admin.register(Datos_Parada)
class Datos_ParadaAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13

@admin.register(Datos_Mapa)
class Datos_MapaAdmin(OSMGeoAdmin):
	default_lon = -6403019.37589
	default_lat = -2909670.42369
	default_zoom = 13