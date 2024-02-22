from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'descricao', 'preco', 'imagem']
        #fields = ['nome', 'descricao']
