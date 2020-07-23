from django.shortcuts import render

def login(request):
	template_name = 'accounts/login.html'
	context = {

	}
	return render(request, template_name, context)