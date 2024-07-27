from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('knowledge_area.urls')),

    path('api/v1/', include('matters.urls')),

    path('api/v1/', include('books.urls')),
    
    path('api/v1/', include('writers.urls')),
    
    path('api/v1/', include('reviews.urls')),
]
