from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from . import views


#Pagina do REST API
router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('router', include(router.urls)),
    path('items/', views.items, name='items'), #precisa do / no final
    path('', views.home, name='home'),
]
