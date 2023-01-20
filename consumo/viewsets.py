from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerializer, PessoasSexosSerializer
from consumo.models import Pessoas


class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer

    def get_queryset(self):
        return Pessoas.objects.all().filter(cidade='Meeren', sexo='F')


class PessoasSexosViewSet(ModelViewSet):
    serializer_class = PessoasSexosSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        sexo = query_params.get('sexo', None)
        if sexo is not None:
            return Pessoas.objects.all().order_by('-nascimento').filter(sexo=sexo.upper())
        return Pessoas.objects.all().order_by('-nascimento')