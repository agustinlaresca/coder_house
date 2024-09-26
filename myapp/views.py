from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm
from .models import Book

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_author')
    else:
        form = AuthorForm()
    return render(request, 'myapp/author_form.html', {'form': form})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_book')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'myapp/search_books.html', {'books': books, 'query': query})