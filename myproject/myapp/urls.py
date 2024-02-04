from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from . import views
from django.contrib.auth.views import LogoutView


#Pagina do REST API
router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('router', include(router.urls)),
    path('items/', views.items, name='items'), #precisa do / no final
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
]
