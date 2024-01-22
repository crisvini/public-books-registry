from django.urls import path
from .views import index, novo

urlpatterns = [
    path('', index, name='index'),
    path('novo', novo, name='novo'),
]
