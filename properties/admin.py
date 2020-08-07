from django.contrib import admin
from .models import Property, Appartment, House, OccupiedHouse

admin.site.register(Property)
admin.site.register(Appartment)
admin.site.register(House)
admin.site.register(OccupiedHouse)