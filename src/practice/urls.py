from django.contrib import admin
from django.urls import path

from store.views import books, book

urlpatterns = [
    path('', books, name="home"),
    path('<int:book_pk>/', book, name="book"),
    path('admin/', admin.site.urls),
]
