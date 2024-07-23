from django.contrib import admin
from matters.models import Matter

@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ('id', 'matter', 'author','nationality' )