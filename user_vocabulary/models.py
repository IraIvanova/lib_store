from django.db import models
from django.conf import settings


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    locale = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class UserVocabulary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'word']

    def __str__(self):
        return f'{self.user.username} - {self.word}'