from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from properties.models import House, Appartment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages

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

def house_report(request):
	occupied_houses = House.objects.filter(vacant=False)
	vacant_houses = House.objects.filter(vacant=True)
	appartments = Appartment.objects.all()

	from_email = 'lhirani9@gmail.com'
	to = request.user.email

	subject = 'House Report'
	text_content = 'House Report'

	html_content = render_to_string('email/house_report.html', {
		'username': request.user.username,
		'occupied_houses': occupied_houses,
		'appartments': appartments,
		'vacant_houses': vacant_houses,
		}
	)

	if html_content:
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.content_subtype = "html"
		msg.send()
		messages.success(request, 'Your report has been successfully generated. Kindly check your email')

		return redirect('dashboard:dashboard')


