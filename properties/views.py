from django.shortcuts import render
from .models import Property
from django.db.models import Q
from .forms import PropertyCreateForm
from django.contrib import messages

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

def property_create(request):
	template_name = 'properties/property_create.html'
	if request.method == 'POST':
		form = PropertyCreateForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Your property has been created!'))
	else:
		form = PropertyCreateForm(label_suffix='')

	context = {
		'form': form,
	}

	return render(request, template_name, context)