from django.contrib import admin
from app.models import ControleFinanceiro

class ControleFinanceiroAdmin(admin.ModelAdmin):
    list_display = []
    for field in ControleFinanceiro._meta.fields:
        list_display.append(field.name)

admin.site.register(ControleFinanceiro, ControleFinanceiroAdmin)
