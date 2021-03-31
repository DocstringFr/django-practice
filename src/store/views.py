from django.shortcuts import get_object_or_404, render

from store.forms import AddBookForm
from store.models import Book


def books(request):
    form = AddBookForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'store/index.html', context={"books": Book.objects.all(),
                                                        "form": form})


def book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, 'store/book.html', context={"book": book})
