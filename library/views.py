from django.shortcuts import render
from .forms import BookForms


def index(request):
    return render(request, 'library/index.html')


def novo(request):
    form = BookForms

    return render(request, 'library/novo.html', {'form': form})
