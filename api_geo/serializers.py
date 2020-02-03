from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Datos_Parada, Datos_Mapa, Parada

class ParadaSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Parada
		geo_field = 'location_parada'
		fields = '__all__'

class Datos_MapaSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Datos_Mapa
		geo_field = 'location_bus'
		fields = '__all__'

class Datos_ParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datos_Parada
		fields = '__all__'

