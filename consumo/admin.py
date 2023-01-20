from django.contrib import admin
from consumo.models import Pessoas
from import_export.admin import ImportExportModelAdmin

class PessoaAdmin(ImportExportModelAdmin):
    list_display = ('id_cold', 'nome', 'sobrenome','sexo', 'altura', 'peso', 'nascimento', 'bairro', 'cidade', 'estado', 'numero',)

admin.site.register(Pessoas, PessoaAdmin)