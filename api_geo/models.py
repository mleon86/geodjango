from django.contrib.gis.db import models


# Create your models here.
#Datos de las Paradas
class Parada(models.Model):
	nombre = models.CharField(max_length = 10, blank = False, null = False)
	location_parada = models.PointField()

	class Meta:
		verbose_name = 'Parada'
		verbose_name_plural = 'Paradas'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

class Datos_Parada(models.Model): #datos que envia la parada
	time_rasp_parada = models.DateTimeField(auto_now_add = False) #tiempo que provee el raspberry de la parada
	time_created_parada = models.DateTimeField(auto_now_add = True)#tiempo en el que se guarda en la base de datos
	siniestro_parada = models.BooleanField(default = False)#boton de siniestro en la parada
	prep_asiento = models.BooleanField(default = False)#boton para solicitar asiento para personas con discapacidad
	
	class Meta:
		verbose_name = 'Datos_Parada'
		verbose_name_plural = 'Datos_Paradas'
		ordering = ['time_rasp_parada']

	def __str__(self):
		return self.id_parada

class Datos_Mapa(models.Model): #datos que envia la parada
	bus = models.CharField(max_length = 10, blank = False, null = False)
	location_bus = models.PointField()
	
	class Meta:
		verbose_name = 'Datos_Mapa'
		verbose_name_plural = 'Datos_Mapas'
		ordering = ['bus']

	def __str__(self):
		return self.bus