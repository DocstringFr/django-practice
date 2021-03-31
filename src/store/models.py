from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    wikipedia = models.URLField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    ADVENTURE = "AV"
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"

    GENRES = [
        (ADVENTURE, "Aventure"),
        (THRILLER, "Thriller"),
        (FANTASY, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-fiction"),
    ]

    title = models.CharField(max_length=300)
    price = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, choices=GENRES)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
