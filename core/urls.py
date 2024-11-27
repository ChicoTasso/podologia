from django.urls import path, include
from .views import ListaPodologos
from rest_framework.routers import DefaultRouter
from . import views

# Roteador para as APIs
router = DefaultRouter()
router.register(r'podologos', ListaPodologos)

urlpatterns = [
    path('api/', include(router.urls))
]
