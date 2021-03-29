import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practice.settings")

import django

django.setup()

from store.models import Author, Book

authors = [
    {"firstname": "Henri", "lastname": "Beyle", "wikipedia": "https://fr.wikipedia.org/wiki/Stendhal"},
    {"firstname": "Victor", "lastname": "Hugo", "wikipedia": "https://fr.wikipedia.org/wiki/Victor_Hugo"},
    {"firstname": "Alexandre", "lastname": "Dumas", "wikipedia": "https://fr.wikipedia.org/wiki/Alexandre_Dumas"},
    {"firstname": "Isaac", "lastname": "Asimov", "wikipedia": "https://fr.wikipedia.org/wiki/Isaac_Asimov"},
]

books = [
    {"title": "Les Trois Mousquetaires", "price": 7.95,
     "summary": "Les Trois Mousquetaires est le plus célèbre des romans d'Alexandre Dumas père, initialement publié en feuilleton dans le journal Le Siècle de mars à juillet 1844, puis édité en volume dès 1844 aux éditions Baudry et réédité en 1846 chez J. B. Fellens et L. P. Dufour avec des illustrations de Vivant Beaucé. Il est le premier volet de la trilogie romanesque dite « des mousquetaires », à laquelle il donne son nom, suivi par Vingt Ans après (1845) et Le Vicomte de Bragelonne (1847).",
     "author": 3, "category": Book.ADVENTURE, "stock": 12},
    {"title": "Les Robots", "price": 12.99,
     "summary": "Les Robots (titre original : I, Robot) est un recueil de neuf nouvelles de science-fiction écrites par Isaac Asimov, publié la première fois par Gnome Press en 1950 et traduit en France en 1967.",
     "author": 4, "category": Book.SCIENCE_FICTION, "stock": 0},
    {"title": "Fondation", "price": 14.99,
     "summary": "Fondation (titre original : Foundation) est un roman de science-fiction rédigé par Isaac Asimov et composé de cinq nouvelles, dont quatre publiées individuellement entre 1942 et 1944 dans la revue Astoundinng Science-Fiction et à laquelle une cinquième fut ajoutée pour former ce livre publié pour la première fois en 19511. C'est le premier volet du Cycle de Fondation. Bien qu’il constitue aujourd'hui le troisième épisode chronologique de ce cycle, il est le premier à avoir été écrit et peut donc être lu indépendamment de Prélude à Fondation et L'Aube de Fondation.",
     "author": 4, "category": Book.SCIENCE_FICTION, "stock": 15},
    {"title": "L'homme qui rit", "price": 12.99,
     "summary": "L'Homme qui rit est un roman philosophique de Victor Hugo publié en avril 1869 dont l’action se déroule dans l’Angleterre de la fin du xviie et du début du xviiie siècle. Il est notamment célèbre pour la figure mutilée dans un rire permanent de son héros qui a fortement inspiré le monde littéraire et cinématographique.",
     "author": 2, "category": Book.ADVENTURE, "stock": 0},
    {"title": "Notre-Dame de Paris", "price": 8.99,
     "summary": "Notre-Dame de Paris (titre complet : Notre-Dame de Paris. 1482) est un roman historique de l'écrivain français Victor Hugo, publié en 1831.",
     "author": 2, "category": Book.ADVENTURE, "stock": 24},
    {"title": "Le Rouge et le Noir", "price": 21.95,
     "summary": "Le Rouge et le Noir, sous-titré Chronique du xixe siècle, puis Chronique de 1830, est un roman écrit par Stendhal, publié pour la première fois à Paris chez Levasseur le 13 novembre 18301, bien que l'édition originale2 mentionne la date de 1831. C'est son deuxième roman, après Armance.",
     "author": 1, "category": Book.ADVENTURE, "stock": 8},
    {"title": "La Chartreuse de Parme", "price": 18.95,
     "summary": "La Chartreuse de Parme est un roman publié par Stendhal. Cette œuvre majeure, qui lui valut la célébrité, fut publiée en deux volumes en mars 1839, puis refondue en 1841, soit peu avant la mort de Stendhal, à la suite d'un article fameux de Balzac1 et prenant de fait un tour plus « balzacien » : aujourd’hui, c’est le texte stendhalien d’origine qu’on lit encore.",
     "author": 1, "category": Book.ADVENTURE, "stock": 7},
]

for author in authors:
    Author.objects.get_or_create(**author)

for book in books:
    book_author_id = book.pop("author")
    book_instance, created = Book.objects.get_or_create(**book)
    author = Author.objects.get(pk=book_author_id)
    if author:
        book_instance.author = author
        book_instance.save()
