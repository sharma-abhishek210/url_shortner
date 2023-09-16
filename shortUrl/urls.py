from django.urls import path
from .views import URLShortener

urlpatterns = [
    path('<str:short_url>/', URLShortener.as_view(), name='redirect_short_url'),
    path('createShortURL', URLShortener.as_view(), name='create_short_url'),
]