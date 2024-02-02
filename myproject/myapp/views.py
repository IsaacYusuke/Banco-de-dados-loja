from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

def home(request):
    # seu código de lógica
    return render(request, 'myapp/home.html', {'var1': 'valor1'})

#Pagina do REST API
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

