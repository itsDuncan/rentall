from django.urls import re_path
from .import views

app_name = 'dashboard'

urlpatterns = [
	re_path(r'^$', views.dashboard, name='dashboard'),
	re_path(r'^tenants/$', views.tenants, name='tenant-list'),
]