from django.contrib import admin
from app.models import ControleColeta

class ControleColetaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ControleColeta._meta.fields :
        list_display.append(field.name)

admin.site.register(ControleColeta, ControleColetaAdmin)
