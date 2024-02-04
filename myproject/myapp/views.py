from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
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

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = UserCreationForm()
    return render(request, 'myapp/cadastro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


#Pagina do REST API
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

