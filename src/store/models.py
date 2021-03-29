from django.db import models
import uuid


class Author(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    wikipedia = models.URLField(blank=True)


class Book(models.Model):
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"

    GENRES = [
        (THRILLER, "Thriller"),
        (FANTASY, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-fiction"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300, blank=False)
    price = models.FloatField(blank=True)
    summary = models.TextField(blank=True)
    author = models.ManyToManyField(Author, blank=True)
    category = models.CharField(max_length=25, blank=True, choices=GENRES)
    stock = models.IntegerField(default=0)
