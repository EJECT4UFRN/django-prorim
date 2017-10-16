from django.contrib import admin
from app.models import ChoiceStatusManutencaoCorretiva

class ChoiceStatusManutencaoCorretivaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ChoiceStatusManutencaoCorretiva._meta.fields:
        list_display.append(field.name)

admin.site.register(ChoiceStatusManutencaoCorretiva, ChoiceStatusManutencaoCorretivaAdmin)
