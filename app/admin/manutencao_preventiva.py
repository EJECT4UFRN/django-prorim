from django.contrib import admin
from app.models import ManutencaoPreventiva

class  ManutencaoPreventivaAdmin(admin.ModelAdmin):
    list_display = []
    for field in ManutencaoPreventiva._meta.fields :
        list_display.append(field.name)

admin.site.register(ManutencaoPreventiva, ManutencaoPreventivaAdmin)