from django.shortcuts import render

# Create your views here.
def Home(request):
	return render(request, 'index.html')

def Map(request):
	return render(request, 'world/map.html')