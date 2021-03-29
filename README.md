# Exercices Django

## Les modèles

L'objectif de cet exercice est de créer un modèle pour représenter les livres du site d'une bibliothèque en ligne.

Votre modèle devra contenir les champs suivants :
- `id` : Un identifiant unique qui servira de clé primaire (utilisez le module uuid)
- `title` : Le titre du livre
- `price` : Le prix du livre (nombre décimal)
- `summary` : Le résumé du livre
- `author` : L'auteur du livre (clé étrangère avec une relation Many to Many)
- `category` : La catégorie (avec les choix suivants : **thriller**, **fantastique**, **romance**, **horreur**, **science-fiction**)
- `stock` : La quantité en stock (avec une valeur par défaut de 0)


Vous devrez également créer un modèle pour représenter les auteurs avec les champs pour :
- `firstname` : Le prénom
- `lastname` : Le nom de famille
- `wikipedia` : Une URL vers la page wikipédia de l'auteur