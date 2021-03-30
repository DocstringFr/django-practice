# Exercices Django

## Les templates

Le but de cet exercice est de remplacer les fonctions `HttpResponse` dans les vues ([src/store/views.py](src/store/views.py)) par des templates HTML.

Vous devez créer un template `index.html` et un template `book.html` pour les vues `books` et `book`.

### index.html

La page d'index doit afficher chaque titre de livre dans une balise `<h1>`.

### book.html

La page d'un livre doit afficher le titre du livre dans une balise `<h1>`, l'auteur du livre dans une balise `<h5>`.

Le titre du livre doit être automatiquement converti en format 'titre anglophone' (première lettre de chaque mot en majuscule) grâce au filtre [title](https://docs.djangoproject.com/fr/3.1/ref/templates/builtins/#title).

Vous devez également afficher le résumé du livre (champ `summary`) dans une balise `<p>`.

# Solution

Première étape pour utiliser des fichiers de gabarits, créer le dossier `templates` à l'intérieur de notre application `store` : [src/store/templates](src/store/templates).

À l'intérieur d'un sous-dossier du nom de notre application, nous créons donc deux fichiers HTML :
- [src/store/templates/store/index.html](src/store/templates/store/index.html)
- [src/store/templates/store/book.html](src/store/templates/store/book.html)

Nous retournons ces fichiers HTML dans les vues correspondantes ([src/store/views.py](src/store/views.py)) avec la fonction `render` et en passant les données à afficher au paramètre contexte :

```
def books(request):
    return render(request, 'store/index.html', context={"books": Book.objects.all()})


def book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, 'store/book.html', context={"book": book})
```

Nous pouvons ensuite utiliser le langage de gabarits de Django pour boucler sur les livres envoyés au contexte dans le fichier `index.html` :
```
{% for book in books %}
    <h1>{{ book.title }}</h1>
{% endfor %}
```

Pour la vue de chaque livre, nous utilisons tout simplement les variables avec les doubles accolades (`{{ var }}`) :
```
<h1>{{ book.title|title }}</h1>
<h5>{{ book.author.firstname }} {{ book.author.lastname }}</h5>
<p>{{ book.summary }}</p>
```

Pour le titre du livre, nous utilisons le filtre `title` (à ne pas confondre avec le champ `title` de la variable `book`).