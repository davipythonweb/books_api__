from django.urls import path
from . import views

app_name = 'namespaceMatter'

urlpatterns = [
    path('matters/', views.MatterCreateListView.as_view(), name='list'),
]