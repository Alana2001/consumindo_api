from django.db import models

SEXO_CHOICES = (
    ('F', 'Feminino'),
    ('M', 'Masculino'),
)

class Pessoas(models.Model):
    id_cold = models.CharField(max_length=9)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    altura = models.CharField(max_length=9)
    peso = models.CharField(max_length=9)
    nascimento = models.DateField()
    bairro = models.CharField(max_length=9)
    cidade = models.CharField(max_length=9)
    estado = models.CharField(max_length=9)
    numero = models.CharField(max_length=9)


    def __str__(self):
        return self.nome

    def get_nascimento(self):
        return self.nascimento.strftime('%d/%m/%Y')
    

