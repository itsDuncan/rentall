from django.urls import re_path

from .import views

app_name = 'accounts'

urlpatterns = [
	re_path(r'^tenant-create/$', views.tenant_create, name='tenant-create'),
]