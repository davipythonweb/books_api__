from django.urls import path
from . import views

app_name = 'namespaceWriters'

urlpatterns = [
    path('writers/', views.WriterCreateListView.as_view(), name='list'),

    path('writers/<int:pk>/', views.WriterRetrieveUpdateDestroyView.as_view(), name='retrieve'),
]