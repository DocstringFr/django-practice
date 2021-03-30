import uuid

from django.shortcuts import HttpResponse, get_object_or_404

from store.models import Book


def books(request):
    books_titles = [book.title for book in Book.objects.all()]

    return HttpResponse("<br>".join(books_titles))


def book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return HttpResponse(book.title)
