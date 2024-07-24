from django.contrib import admin
from writers.models import Writer

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer','nationality' )