from django.urls import path
from .views import index, novo

urlpatterns = [
    path('', index),
    path('novo', novo),
]
