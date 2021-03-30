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