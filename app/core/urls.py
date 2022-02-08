from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

#one Endpoint to handle POST AND GET
urlpatterns = format_suffix_patterns([
    path('', views.api_root),    
    path('api/v1/quotes/',
         views.exchange_endpoint,
         name='exchange-endpoint'),
    
])