from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User

@login_required
def dashboard(request):
	template_name = 'dashboard/dashboard.html'
	context = {}
	return render(request, template_name, context)

def tenants(request):
	template_name = 'dashboard/tenants.html'
	tenants = User.objects.all().filter(landlord=False).exclude(username=request.user)
	context = {
		'tenants': tenants,
	}
	return render(request, template_name, context)