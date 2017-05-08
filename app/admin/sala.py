from django.contrib import admin
from app.models import Sala

class SalaAdmin(admin.ModelAdmin):
    list_display = []
    for field in Sala._meta.fields:
        list_display.append(field.name)

admin.site.register(Sala, SalaAdmin)
