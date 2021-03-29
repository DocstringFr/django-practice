# Exercices Django

## Les modèles

L'objectif de cet exercice est de créer un modèle (que vous appelerez `Book`) pour représenter les livres du site d'une bibliothèque en ligne.

Votre modèle devra contenir les champs suivants :
- `title` : Le titre du livre. Champ obligatoire.
- `price` : Le prix du livre (nombre décimal). Champ facultatif.
- `summary` : Le résumé du livre. Champ facultatif.
- `author` : L'auteur du livre (relation plusieurs-à-un et supression en cascade). Champ facultatif.
- `category` : La catégorie (avec les choix suivants : **Aventure**, **Thriller**, **Fantastique**, **Romance**, **Horreur**, **Science-fiction**). Champ facultatif.
- `stock` : La quantité en stock (avec une valeur par défaut de 0). Champ facultatif.


Vous devrez également créer un modèle (que vous appelerez `Author`) pour représenter les auteurs avec les champs pour :
- `firstname` : Le prénom. Champ obligatoire.
- `lastname` : Le nom de famille. Champ obligatoire.
- `wikipedia` : Une URL vers la page wikipédia de l'auteur. Champ facultatif.

Vous devez également ajouter une méthode sur chaque modèle qui permet d'afficher une représentation des objets en chaîne de caractères.

👉 Pour la classe `Book` vous devez afficher **le titre** du livre.  
👉 Pour la classe `Author` vous devez afficher **le prénom** (`firstname`) et **le nom de famille** (`lastname`).

# Solution

Pour cet exercice, il fallait créer les modèles dans [src/store/models.py](src/store/models.py).

On devait ensuite créer les fichiers de migrations avec la commande `python manage.py makemigrations`.

Pour appliquer les migrations dans la base de données, il fallait ensuite utiliser la commande `python manage.py migrate`.