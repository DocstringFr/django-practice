# Exercices Django

## Les urls dans les templates

Le but de cet exercice est de rajouter les liens vers chaque page individuelle d'un livre (vue `book` dans [src/store/views.py](src/store/views.py)) sur la page d'accueil du site ([index.html](src/store/templates/store/index.html)).

Vous devez également rajouter un lien dans le fichier [base.html](src/store/templates/store/base.html) qui permette de rediriger vers l'accueil du site depuis n'importe quelle page.

# Solution

Pour résoudre cet exercice, il fallait déjà donner un nom à nos chemins d'URL dans le fichier [urls.py](src/practice/urls.py) en utilisant le paramètre `name` de la fonction `path` :

```
urlpatterns = [
    path('', books, name="home"),
    path('<int:book_pk>/', book, name="book"),
    path('admin/', admin.site.urls),
]
```

Pour le reste, il suffisait d'utiliser la balise `{% url %}` pour rajouter des liens dans nos fichiers HTML :

### `base.html`

On rajoute un lien vers la page d'accueil dans le fichier de base qui sert de template à tous les autres fichiers HTML du site :
```
<a href="{% url 'home' %}">Accueil</a>
```

### `index.html`

On rajoute un lien sur les titres en indiquant la clé primaire de chaque livre dans le paramètre `book_pk` de l'URL (`book_pk=book.pk`) :
```
{% for book in books %}
    <h1><a href="{% url 'book' book_pk=book.pk %}">{{ book.title }}</a></h1>
{% endfor %}
```