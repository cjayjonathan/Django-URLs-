from django.db import models
from django.conf import settings

# Create your models here.
class TitleModel(models.Model):
    title = models.CharField(max_length=100)

class TextModel(models.Model):
    text = models.TextField()

class AuthorModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

class CreatedModel(models.Model):
    created_date = models.DateTimeField()

class PublishedModel(models.Model):
    published_date = models.DateTimeField()