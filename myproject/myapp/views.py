from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

def home(request):
    # seu código de lógica
    return render(request, 'myapp/home.html', {})

def items(request):
    # seu código de lógica
    items = Item.objects.all()
    return render(request, 'myapp/items.html', {'items': items})

#Pagina do REST API
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

