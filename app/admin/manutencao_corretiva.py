from django.contrib import admin
from app.models import ManutencaoCorretiva

class ManutencaoCorretivaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ManutencaoCorretiva._meta.fields:
        list_display.append(field.name)

admin.site.register(ManutencaoCorretiva, ManutencaoCorretivaAdmin)
