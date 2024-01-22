from django.shortcuts import render, redirect
from .forms import BookForms


def index(request):
    return render(request, 'library/index.html')


def novo(request):
    form = BookForms
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, 'library/novo.html', {'form': form})
