from django.contrib import admin
from app.models import Erro

class ErroAdmin(admin.ModelAdmin):
    list_display = []
    for field in Erro._meta.fields :
        list_display.append(field.name)

admin.site.register(Erro, ErroAdmin)
