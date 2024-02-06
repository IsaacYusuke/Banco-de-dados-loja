from django.contrib import admin

# Register your models here.
from .models import Item

admin.site.register(Item)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco', 'imagem']