from django.urls import path
from .views import Home, Map

urlpatterns = [
	path('', Home, name = 'index'),
	path('maps/', Map, name = 'map')
]