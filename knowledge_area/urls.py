from django.urls import path
from. import views

app_name = 'namespaceKnowledgeArea'

urlpatterns = [
    
    path('knowledge_area/', views.KnowledgeAreaCreateListView.as_view(), name='list'),
]
