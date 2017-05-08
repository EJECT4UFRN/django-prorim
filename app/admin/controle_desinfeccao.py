from django.contrib import admin
from app.models import ControleDesinfeccao

class ControleDesinfeccaoAdmin(admin.ModelAdmin):
    list_display = []
    for field in ControleDesinfeccao._meta.fields :
        list_display.append(field.name)

admin.site.register(ControleDesinfeccao, ControleDesinfeccaoAdmin)
