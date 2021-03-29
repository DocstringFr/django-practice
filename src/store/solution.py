# Ne modifiez pas les lignes ci-dessous
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practice.settings")

import django

django.setup()
# Ne modifiez pas les lignes ci-dessus


# L'exercice commence ici
from store.models import Author, Book

# Créer des données
"""- Créez le livre « Les Misérables » et son auteur associé (Victor Hugo).
    - Le livre doit avoir un prix de 4,95€.
    - Le livre n'a pas de catégorie associée.
    - Pour le résumé et le nombre d'exemplaires en stock, vous pouvez mettre les valeurs que vous souhaitez.
"""
author, created = Author.objects.get_or_create(firstname="Victor",
                                               lastname="Hugo",
                                               wikipedia="https://fr.wikipedia.org/wiki/Victor_Hugo")

Book.objects.get_or_create(title="Les Misérables",
                           author=author,
                           price=4.95,
                           category=Book.ADVENTURE,
                           summary="Dans ce roman emblématique de la littérature française qui décrit la vie de pauvres gens dans Paris et la France provinciale du xixe siècle, l'auteur s'attache plus particulièrement au destin du bagnard Jean Valjean. C'est un roman historique, social et philosophique dans lequel on retrouve les idéaux du romantisme et ceux de Victor Hugo concernant la nature humaine.",
                           stock=5)

# Récupérer des données
# - Récupérer tous les livres dont le nombre d'exemplaires en stock est de 0.
empty_stocks = Book.objects.filter(stock=0)
print(f"Livres à racheter : {[book.title for book in empty_stocks]}.")

# - Récupérer tous les livres dont le prix est strictement inférieur à 10€.
cheap_books = Book.objects.filter(price__lt=10)
print(f"Les livres dont le prix est inférieur à 10€ sont : {[book.title for book in cheap_books]}.")

# - Récupérer tous les livres de Victor Hugo.
victor_hugo = Author.objects.get(firstname="Victor", lastname="Hugo")
if victor_hugo:
    victor_hugo_books = Book.objects.filter(author=victor_hugo)
    print(f"Livres écrits par Victor Hugo : {[book.title for book in victor_hugo_books]}.")

# - Récupérer le nom de l'auteur du livre « Les Trois Mousquetaires ».
les_trois_mousquetaires = Book.objects.get(title="Les Trois Mousquetaires")
author = les_trois_mousquetaires.author
print(f"Les Trois Mousquetaires a été écrit par {author.firstname} {author.lastname}.")

# - Récupérer la valeur totale du stock de la bibliothèque (le prix de tous les livres).
all_books = Book.objects.filter(stock__gt=0)
total_price = sum(book.price * book.stock for book in all_books)
print(f"Valeur totale du stock : {round(total_price, 2)}€.")

# - Récupérer le nombre total de livres dans la bibliothèque (le stock de tous les livres).
all_books = Book.objects.filter(stock__gt=0)
total_books = sum(book.stock for book in all_books)
print(f"Nombre de livres en stock : {total_books}.")

# Supprimer des données
# - Supprimez tous les livres de Victor Hugo.
victor_hugo_books = Book.objects.filter(author__lastname="Hugo", author__firstname="Victor")
victor_hugo_books.delete()
