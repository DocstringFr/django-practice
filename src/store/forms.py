from django.forms import ModelForm
from store.models import Book


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
