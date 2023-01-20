from rest_framework import serializers
from consumo.models import Pessoas

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ('id_cold', 'nome', 'sobrenome', 'sexo', 'altura', 'peso', 'nascimento', 'bairro', 'cidade', 'estado', 'numero',)

class PessoasSexosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ('id_cold', 'nome', 'sobrenome', 'sexo', 'altura', 'peso', 'nascimento', 'bairro', 'cidade','estado', 'numero')