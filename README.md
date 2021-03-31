# Exercices Django

## Les formulaires

Le but de cet exercice est de rajouter un formulaire sur la page d'accueil du site ([index.html](src/store/templates/store/index.html)) qui permette à un utilisateur administrateur de rajouter un livre dans la base de données.

# Solution

La première chose à faire était de créer un fichier [forms.py](src/store/forms.py) dans lequel créer la classe pour le formulaire :

```
from django.forms import ModelForm
from store.models import Book


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
```

Rien de très compliqué ici, on importe la classe `ModelForm` et le modèle `Book`.

On crée ensuite un formulaire pour le modèle en indiquant que nous souhaitons utiliser tous les champs (grâce à la chaîne de caractères `'__all__'`).

Dans la vue [books](src/store/models.py) on crée un formulaire à partir de notre classe.
On passe `request.POST or None` au formulaire : si des données sont soumises via le formulaire, on les récupères dans `request.POST`, sinon on initialise un formulaire vide.

Si le formulaire et les données sont valides, on sauve le formulaire (et donc l'instance du livre) dans la base de données. 

On passe ensuite le formulaire au contexte dans la variable `form`.

```
def books(request):
    form = AddBookForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'store/index.html', context={"books": Book.objects.all(),
                                                        "form": form})
```

On peut ainsi ajouter le formulaire grâce à cette variable dans le template `index.html` :
```
{% block content %}
    {% for book in books %}
        <h1><a href="{% url 'book' book_pk=book.pk %}">{{ book.title }}</a></h1>
    {% endfor %}

    <!-- FORMULAIRE -->
    <h1>Ajouter un livre</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Ajouter">
    </form>
{% endblock %}
```