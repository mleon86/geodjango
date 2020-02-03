from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.gis.measure import D
from django.contrib.gis.db.models import functions

#from rest_framework.viewsets import ReadOnlyModelViewSet
#from rest_framework_gis.filters import InBBoxFilter
from .models import Datos_Mapa, Parada, Datos_Parada
from .serializers import Datos_MapaSerializer, ParadaSerializer, Datos_ParadaSerializer

class Datos_MapaList(APIView):
	def get(self, request, nombre):
		parada = get_object_or_404(Parada, nombre = nombre)
		geom = parada.location_parada
		lista_buses = Datos_Mapa.objects.filter(location_bus__distance_lt = (geom, D(km=2)))
		data = Datos_MapaSerializer(lista_buses, many = True).data
		return Response(data)