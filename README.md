# Exercices Django

## Les templates

Le but de cet exercice est de créer un héritage de templates pour éviter de répéter les balises HTML `doctype`, `html`, `head` et `body` sur les pages [index.html](src/store/templates/store/index.html) et [book.html](src/store/templates/store/book.html).

Vous devez donc créer un fichier `base.html` que les deux fichiers `index.html` et `book.html` viendront étendre à l'aide de deux balises `block` (une pour pouvoir modifier la balise HTML `<title>` sur chaque page et une pour pouvoir insérer du contenu à l'intérieur de la balise `<body>`).

# Solution

La première étape était de créer un fichier `base.html` dans le dossier [src/store/templates/store](src/store/templates/store).

À l'intérieur de ce fichier, il fallait placer la base d'un fichier HTML et deux balises `{% block %}` pour pouvoir étendre le fichier HTML par la suite :

```
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    {% block title %}
    {% endblock %}
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

Ensuite, à l'intérieur des fichiers [index.html](src/store/templates/store/index.html) et [book.html](src/store/templates/store/book.html) il fallait utiliser la balise `{% extends %}` pour étendre ce fichier et insérer les données des pages respectives :

### `index.html`

```
{% extends 'store/base.html' %}

{% block title %}
    <title>La bibliothèque</title>
{% endblock %}

{% block content %}
    {% for book in books %}
        <h1>{{ book.title }}</h1>
    {% endfor %}
{% endblock %}
```

### `book.html`

```
{% extends 'store/base.html' %}

{% block title %}
    <title>{{ book.title }}</title>
{% endblock %}

{% block content %}
    <h1>{{ book.title|title }}</h1>
    <h5>{{ book.author.firstname }} {{ book.author.lastname }}</h5>
    <p>{{ book.summary }}</p>
{% endblock %}
```

