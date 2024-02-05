from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

    def __str__(self):
        return self.nome

