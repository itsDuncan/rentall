from django.shortcuts import render, redirect
from .forms import RegisterTenantForm
from django.contrib import messages

def tenant_create(request):
	template_name = 'accounts/tenant_create.html'

	if request.method == 'POST':
		form = RegisterTenantForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, 'New tenant has been created!')
			return redirect('dashboard:tenant-list')
	else:
		form = RegisterTenantForm(label_suffix='')

	context = {
		'form': form,
	}
	return render(request, template_name, context)