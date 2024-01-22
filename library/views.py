from django.shortcuts import render


def index(request):
    return render(request, 'library/index.html')


def novo(request):
    return render(request, 'library/novo.html')