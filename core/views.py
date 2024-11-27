from .models import ProfissionalDePodologia
from .serializers import ProfissionalDePodologiaSerializer
from rest_framework import viewsets


class ListaPodologos(viewsets.ModelViewSet):    
    queryset = ProfissionalDePodologia.objects.all()
    serializer_class = ProfissionalDePodologiaSerializer