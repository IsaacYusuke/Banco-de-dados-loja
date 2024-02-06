from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    imagem = models.ImageField(upload_to='item_images/', null=True)  # As imagens serão salvas na pasta 'item_images'

    def __str__(self):
        return self.nome

