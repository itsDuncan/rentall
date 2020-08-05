from django.shortcuts import render
from properties.models import Property

def home(request):
	template_name = 'home/home.html'
	properties = Property.objects.all()

	context = {
		'properties': properties,
	}
	
	return render(request, template_name, context)