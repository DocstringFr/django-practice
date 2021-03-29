# Exercices Django

## Les modèles

L'objectif de cet exercice est de créer un modèle (que vous appelerez `Book`) pour représenter les livres du site d'une bibliothèque en ligne.

Votre modèle devra contenir les champs suivants :
- `id` : Un identifiant unique qui servira de clé primaire (utilisez le module uuid)
- `title` : Le titre du livre
- `price` : Le prix du livre (nombre décimal)
- `summary` : Le résumé du livre
- `author` : L'auteur du livre (clé étrangère avec une relation Many to Many)
- `category` : La catégorie (avec les choix suivants : **Aventure**, **Thriller**, **Fantastique**, **Romance**, **Horreur**, **Science-fiction**)
- `stock` : La quantité en stock (avec une valeur par défaut de 0)


Vous devrez également créer un modèle (que vous appelerez `Author`) pour représenter les auteurs avec les champs pour :
- `firstname` : Le prénom
- `lastname` : Le nom de famille
- `wikipedia` : Une URL vers la page wikipédia de l'auteur

Vous devez également ajouter une méthode sur chaque modèle qui permet d'afficher une représentation des objets en chaîne de caractères.

👉 Pour la classe `Book` vous devez afficher **le titre** du livre.  
👉 Pour la classe `Author` vous devez afficher **le prénom** (`firstname`) et **le nom de famille** (`lastname`).