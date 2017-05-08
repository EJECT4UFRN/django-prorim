from django.contrib import admin
from app.models import ChoiceTesteAgua

class ChoiceTesteAguaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoiceTesteAgua._meta.fields:
        list_display.append(field.name)

admin.site.register(ChoiceTesteAgua, ChoiceTesteAguaAdmin)
