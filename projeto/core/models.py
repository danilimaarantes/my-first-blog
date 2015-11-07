from django.db import models


class Produto (models.Model):
    nome = models.CharField(max_length=30)

# Create your models here.
