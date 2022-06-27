from django.contrib import admin

# Register your models here.
from ordenamiento.models import Parroquia, Barrio

admin.site.register(Parroquia)
admin.site.register(Barrio)
