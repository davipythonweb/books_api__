from django.urls import path
from . import views

app_name = 'namespacegenres'

urlpatterns = [
    path('genres/', views.genres, name='genres'),
]
