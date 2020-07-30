from django.shortcuts import render

def properties(request):
	template_name = 'properties/properties.html'
	context = {

	}

	return render(request, template_name, context)