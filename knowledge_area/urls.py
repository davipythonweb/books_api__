from django.urls import path
from. import views

urlpatterns = [
    
    path('knowledge_area/', views.knowledge_area, name='knowledge_area'),
]
