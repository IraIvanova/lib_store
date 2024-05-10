from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    locale = models.CharField(max_length=10)
    author = models.CharField()

    def __str__(self):
        return self.name
