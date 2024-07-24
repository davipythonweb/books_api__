from django.urls import path
from . import views

app_name = 'namespaceBooks'

urlpatterns = [
    path('books/', views.BookCreateListView.as_view(), name='list'),

    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='retrieve'),
]