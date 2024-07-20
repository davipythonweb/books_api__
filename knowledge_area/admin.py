from django.contrib import admin
from knowledge_area.models import Knowledge_Area

@admin.register(Knowledge_Area)
class KnowledgeAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')