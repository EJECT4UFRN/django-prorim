from django.contrib import admin
from app.models import Estadia

class EstadiaAdmin(admin.ModelAdmin):
    list_display = []
    for field in Estadia._meta.fields :
        list_display.append(field.name)

admin.site.register(Estadia, EstadiaAdmin)
