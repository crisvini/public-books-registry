from django.urls import path
from .views import index, new, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('novo', new, name='novo'),
    path('editar/<int:book_id>/', edit, name='editar'),
    path('excluir/<int:book_id>/', delete, name='excluir'),
]
