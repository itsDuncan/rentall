from django.urls import re_path
from .import views

app_name = 'properties'

urlpatterns = [
	re_path(r'^$', views.properties, name='properties-list'),
	re_path(r'^properties-create/$', views.property_create, name='properties-create'),
]