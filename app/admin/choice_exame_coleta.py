from django.contrib import admin
from app.models import ChoiceExameColeta

class ChoiceExameColetaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoiceExameColeta._meta.fields :
        list_display.append(field.name)

admin.site.register(ChoiceExameColeta, ChoiceExameColetaAdmin)
