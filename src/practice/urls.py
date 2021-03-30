from django.contrib import admin
from django.urls import path

from store.views import books, book

urlpatterns = [
    path('', books),
    path('<int:book_pk>/', book),
    path('admin/', admin.site.urls),
]
