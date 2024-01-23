from django.shortcuts import render, redirect
from library.models import Book
from .forms import BookForms
from django.contrib import messages


def index(request):
    books = Book.objects.order_by('-release_date')
    if 'busca' in request.GET:
        name = request.GET['busca']
        if name:
            books = Book.objects.filter(name__icontains=name)

    return render(request, 'library/index.html', {'books': books})


def new(request):
    form = BookForms
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo livro adicionado com sucesso!')
            return redirect('index')

    return render(request, 'library/novo.html', {'form': form})


def edit(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForms(instance=book)

    if request.method == 'POST':
        form = BookForms(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro editado com sucesso!')
            return redirect('index')

    return render(request, 'library/editar.html', {'form': form, 'book_id': book_id})


def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Livro excluido com sucesso!')
    return redirect('index')
