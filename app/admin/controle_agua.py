from django.contrib import admin
from app.models import ControleAgua

class ControleAguaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ControleAgua._meta.fields :
        list_display.append(field.name)

admin.site.register(ControleAgua, ControleAguaAdmin)
