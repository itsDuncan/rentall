from django.shortcuts import render
from .models import Property
from django.db.models import Q

def properties(request):
	template_name = 'properties/properties.html'
	properties = Property.objects.all()

	query = request.GET.get("q", None)

	if query is not None:
		properties = Property.objects.filter(
			Q(name__icontains=query) |
			Q(address__icontains=query) |
			Q(description__icontains=query)
		)

	context = {
		'properties': properties,
	}

	return render(request, template_name, context)