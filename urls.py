from django.urls import path
from . import views

urlpatterns = [
    path('author/new/', views.create_author, name='create_author'),
    path('book/new/', views.create_book, name='create_book'),
    path('search/books/', views.search_books, name='search_books'),
]