from django.urls import path
from. import views

app_name = 'namespaceKnowledgeArea'

urlpatterns = [
    
    path('knowledge_area/', views.KnowledgeAreaCreateListView.as_view(), name='list'),

    path('knowledge_area/<int:pk>/', views.KnowledgeAreaRetrieveUpdateDestoyView.as_view(), name='detail'),
]
