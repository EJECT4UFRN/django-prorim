from django.contrib import admin
from app.models import ChoiceStatusEstadia

class ChoiceStatusEstadiaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoiceStatusEstadia._meta.fields:
        list_display.append(field.name)

admin.site.register(ChoiceStatusEstadia, ChoiceStatusEstadiaAdmin)
