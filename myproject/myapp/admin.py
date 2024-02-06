from django.contrib import admin
from django.utils.html import format_html
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco', 'image_tag']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" height="150" width="auto" />', obj.imagem.url)
        return "Sem imagem"
    
    image_tag.short_description = 'Imagem'


# Register your models here.
admin.site.register(Item, ItemAdmin)
