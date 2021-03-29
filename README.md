# Exercices Django

## Les requêtes

Pour cet exercice, vous disposez du modèle `Book` et du modèle `Author` définis dans [src/store/models.py](src/store/models.py).

La base de données contient plusieurs livres et auteurs déjà créés.

Pour recréer les données de tests de la base de données, vous pouvez exécuter le script [src/store/create_test_data.py](src/store/create_test_data.py).

Dans cet exercice vous devez :

### Créer des données
- Créez le livre « Les Misérables » et son auteur associé (Victor Hugo).
    - Le livre doit avoir un prix de 4,95€.
    - Le livre est rangé dans la catégorie "Aventure".
    - Pour le résumé vous pouvez mettre la valeur que vous souhaitez.
    - Pour le stock, la bibliothèque dispose de 5 exemplaires.

### Récupérer des données
- Récupérer tous les livres dont le nombre d'exemplaires en stock est de 0.
- Récupérer tous les livres dont le prix est strictement inférieur à 10€.
- Récupérer tous les livres de Victor Hugo.
- Récupérer le nom de l'auteur du livre « Les Trois Mousquetaires ».
- Récupérer la valeur totale du stock de la bibliothèque (le prix de tous les livres * le nombre en stocks).
- Récupérer le nombre total de livres dans la bibliothèque (le stock de tous les livres). 

### Supprimer des données
- Supprimez tous les livres de Victor Hugo.

Vous pouvez utiliser le fichier [solution.py](src/store/solution.py) pour écrire les différentes requêtes demandées ci-dessus.