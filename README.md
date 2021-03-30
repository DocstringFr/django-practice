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