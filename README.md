# Exercices Django

## Les templates

Le but de cet exercice est de créer un héritage de templates pour éviter de répéter les balises HTML `doctype`, `html`, `head` et `body` sur les pages [index.html](src/store/templates/store/index.html) et [book.html](src/store/templates/store/book.html).

Vous devez donc créer un fichier `base.html` que les deux fichiers `index.html` et `book.html` viendront étendre à l'aide de deux balises `block` (une pour pouvoir modifier la balise HTML `<title>` sur chaque page et une pour pouvoir insérer du contenu à l'intérieur de la balise `<body>`).