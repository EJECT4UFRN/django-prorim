from django.contrib import admin
from app.models import TestModel

class TestAdmin(admin.ModelAdmin):
    list_display = []
    for field in TestModel._meta.fields:
        list_display.append(field.name)

admin.site.register(TestModel, TestAdmin)
