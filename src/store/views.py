from django.shortcuts import get_object_or_404, render

from store.models import Book


def books(request):
    return render(request, 'store/index.html', context={"books": Book.objects.all()})


def book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, 'store/book.html', context={"book": book})
