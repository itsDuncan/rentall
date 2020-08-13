from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models import Q
from .models import Property, House
from .forms import PropertyCreateForm, AppartmentCreateForm, HouseCreateForm

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
			return redirect('properties:properties-list')
	else:
		form = PropertyCreateForm(label_suffix='')

	context = {
		'form': form,
	}

	return render(request, template_name, context)

def appartment_create(request):
	template_name = 'properties/appartment_create.html'

	if request.method == 'POST':
		form = AppartmentCreateForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Your appartment has been created!'))
			return redirect('dashboard:dashboard')
	else:
		form = AppartmentCreateForm(label_suffix='')

	context = {
		'form': form,
	}

	return render(request, template_name, context)

def house_create(request):
	template_name = 'properties/house_create.html'

	if request.method == 'POST':
		form = HouseCreateForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('A new house has been created!'))
			return redirect('dashboard:dashboard')
	else:
		form = HouseCreateForm(label_suffix='')

	context = {
		'form': form,
	}

	return render(request, template_name, context)

def property_detail(request, slug):
	template_name = 'properties/property.html'
	house = get_object_or_404(House, slug=slug)

	context = {
		'house': house,
	}

	return render(request, template_name, context)

def generate_invoice(request, slug):
	house = get_object_or_404(House, slug=slug)

	from_email = 'lhirani9@gmail.com'
	to = request.user.email

	subject = 'House Report'
	text_content = 'House Report'

	html_content = render_to_string('email/invoice.html', {
		'username': request.user.username,
		'house': house,
		}
	)

	if html_content:
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.content_subtype = "html"
		msg.send()
		messages.success(request, 'Your invoice has been successfully generated. Kindly check your email')

		return redirect('dashboard:dashboard')