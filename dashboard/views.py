from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from properties.models import House, Appartment

@login_required
def dashboard(request):
	template_name = 'dashboard/dashboard.html'
	occupied_houses = House.objects.filter(vacant=False)
	vacant_houses = House.objects.filter(vacant=True)
	appartments = Appartment.objects.all()

	context = {
		'occupied_houses': occupied_houses,
		'appartments': appartments,
		'vacant_houses': vacant_houses,
	}

	return render(request, template_name, context)

def tenants(request):
	template_name = 'dashboard/tenants.html'
	tenants = User.objects.all().filter(landlord=False).exclude(username=request.user)
	context = {
		'tenants': tenants,
	}
	return render(request, template_name, context)