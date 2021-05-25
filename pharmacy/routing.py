from django.urls import path
from .consumers import WSconsumer

ws_urlpatterns = [
    path('ws/itemsws/', WSconsumer.as_asgi())
]