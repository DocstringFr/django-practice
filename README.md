# Exercices Django

## Les urls

Le but de cet exercice est de rajouter deux chemins d'URLs pour pouvoir accéder aux vues [books](src/store/views.py) et [book](src/store/views.py).


### Page d'accueil du site
La page d'accueil du site (http://127.0.0.1:8000/) doit retourner une page qui affiche les titres de tous les livres de la base de données.

### Pages des livres

On doit également pouvoir accéder à la page d'un livre en particulier en indiquant sont `id` dans la base de données dans l'URL.

Par exemple :   
- http://127.0.0.1:8000/1/ doit afficher une page avec `Les Trois Mousquetaires`.  
- http://127.0.0.1:8000/2/ doit afficher une page avec `Les Robots`.

# Solution

Pour résoudre cet exercice, il fallait inclure deux fonctions `path` à l'intérieur de la liste `urlpatterns` contenue dans le fichier [src/practice/urls.py](src/practice/urls.py) :
```
from store.views import books, book

urlpatterns = [
    path('', books),               # Page d'accueil du site
    path('<int:book_pk>/', book),  # Page individuelle d'un livre
    path('admin/', admin.site.urls),
]
```

La chaîne de caractères vide du premier chemin constitue la page d'accueil du site.

Pour la page individuelle d'un livre, on utilise la syntaxe `<int:book_pk>` pour envoyer le nombre indiqué dans l'URL (`1` dans le cas de http://127.0.0.1:8000/1/) au paramètre `book_pk` de la vue `book` :

```
def book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return HttpResponse(book.title)
```

On peut ainsi récupérer le livre correspondant à la clé primaire envoyée dans l'URL dans la base de donnée et afficher le titre du livre.

Notez qu'on utilise la fonction `get_obect_or_404` du module `django.shortcuts` pour afficher automatiquement une page d'erreur 404 dans le cas où le modèle n'existe pas dans la base de données (par exemple avec http://127.0.0.1:8000/50/).