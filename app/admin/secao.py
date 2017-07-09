from django.contrib import admin
from app.models import Secao

class SecaoAdmin(admin.ModelAdmin):
    list_display = []
    for field in Secao._meta.fields:
        list_display.append(field.name)

admin.site.register(Secao, SecaoAdmin)
