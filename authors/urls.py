from django.urls import path
from . import views

app_name = 'namespaceAuthors'

urlpatterns = [
    path('authors/', views.AuthorCreateListView.as_view(), name='list'),

    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='retrieve'),
]