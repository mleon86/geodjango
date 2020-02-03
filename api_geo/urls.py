"""from rest_framework.routers import DefaultRouter
from .views import Datos_MapaSet

router = DefaultRouter()
router.register(r'markers', Datos_MapaSet, basename = 'marker')
urlpatherns = router.urls
"""

from django.urls import path
from .views import Datos_MapaList

urlpatterns = [
	path('maps_consulta/<nombre>/', Datos_MapaList.as_view(), name = 'maps_list')
	]