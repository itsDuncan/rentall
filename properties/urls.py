from django.urls import re_path
from .import views

app_name = 'properties'

urlpatterns = [
	re_path(r'^$', views.properties, name='properties-list'),
	re_path(r'^properties-create/$', views.property_create, name='properties-create'),
	re_path(r'^property/(?P<slug>[\w-]+)/$', views.property_detail, name='properties-detail'),
	re_path(r'^appartment-create/$', views.appartment_create, name='appartment-create'),
	re_path(r'^house-create/$', views.house_create, name='house-create'),
	re_path(r'^generate-invoice/(?P<slug>[\w-]+)/$', views.generate_invoice, name='generate-invoice'),
]