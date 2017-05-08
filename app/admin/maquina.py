from django.contrib import admin
from app.models import Maquina

class MaquinaAdmin(admin.ModelAdmin):
    list_display = []
    for field in Maquina._meta.fields :
        list_display.append(field.name)

admin.site.register(Maquina, MaquinaAdmin)
