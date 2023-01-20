# DESAFIO CONSUMINDO ARQUIVOS

## Desenvolvedora:
+ Discente: Alana Letícia Lustosa de Castro
+ IFPI - Instituto Federal do Piauí - Campus Corrente
+ Docente: @fgsantosti

## Informações do Projeto:
+ Você recebeu um arquivo com dados de alguns clientes que precisam ser importadas
para um banco de dados. Será necessária a criação de dois endpoints para que os
dados sejam consumidos. O arquivo data.xlsx está disponível para realizar os seus
testes necessários.

## Faça as seguintes etapas:
 Criando pasta:
 ```python
 mkdir consumotest2
```

Entrar na pasta:
```python
 cd consumotest2
```

## Criando o ambiente virtual:
Faça o seguinte comando:
```python
 virtualenv env
```

Ative o seu Ambiente Virtual:
```python
 . env/Scripts/activate
```

## Instale o framework Django::
Faça o comando:
```python
 pip install django
```

## Criando o projeto Django Clinica Api:
Use o seguinte comando para criar a config:
```python
 django-admin startproject core .
```

## Mudando as configurações dentro do core:
```python
 LANGUAGE_CODE = 'en-us'
 TIME_ZONE = 'UTC'
```

## Instalando o Django Rest Framework:
```python
 pip install djangorestframework
 ```

## Instalando o Markdown:
```python
 pip install markdown
 ```

## Instalando o django-filter:
```python
 pip install django-filter
```

## Criando a primeira aplicação:
```python
python manage.py startapp consumo
```

## Realizando a instalação das app's criadas:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #framework
    'consumo', 
]
```
## Criando os modelos para nosso api
+ Primeira etapa do nosso modelo de consumo:
```python
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
```

## Criando tabelas para nossos modelos no banco de dados:
+ O último passo é adicionar nosso novo modelo ao banco de dados. 

```python
python manage.py makemigrations consumo
```

O Django preparou um arquivo de migração que precisamos aplicar ao nosso banco de dados:

```python
python manage.py migrate 
```

## Django Admin:
+ Vamos criar um administrador:
```python
python manage.py createsuperuser
```

## Configure o seu arquivo consumo/admin.py
```python
from django.contrib import admin
from consumo.models import Pessoas
from import_export.admin import ImportExportModelAdmin

class PessoaAdmin(ImportExportModelAdmin):
    list_display = ('id_cold', 'nome', 'sobrenome','sexo', 'altura', 'peso', 'nascimento', 'bairro', 'cidade', 'estado', 'numero',)

admin.site.register(Pessoas, PessoaAdmin)
```

## Vamos startar o servidor web:
```python
python manage.py runserver #startando o servidor
```

+ Vamos acessar a área do administrador do sistema que já vem prontinho para gente graças ao framework Django, para isso iremos usamos o segunte endereço no navegador de sua preferência:
```python
http://127.0.0.1:8000/admin/
```

## Serialização:
Crie um arquivo no diretório de medicos denominado serializers.py (consumo/serializer.py) e adicione o seguinte código.

```python
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
```

## Templates - criei uma pasta clamada Tempaltes e logo junto dela criei outra pasta chamada "consumo":

Templates/consumo:

e criei dentro dqa pesta consumo, um arquivo chamado index.html.

Onde coloquei o seguinte código:

```python
<html><head>
    <title>
        Excel file upload and processing : Django Example : ThePythonDjango.Com
    </title>
</head>
<body style="margin-top: 30px;margin-left: 30px;">
    <form action="{% url "consumo:index" %}" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <input type="file" title="Upload excel file" name="excel_file" style="border: 1px solid black; padding: 5px;" required="required">
        <p>
        <input type="submit" value="Upload" style="border: 1px solid green; padding:5px; border-radius: 2px; cursor: pointer;">
    </p></form>

    <p></p>
    <hr>

    {% for row in excel_data %}
        {% for cell in row %}
            {{ cell }}&nbsp;&nbsp;
        {% endfor %}
        <br>
    {% endfor %}


</body></html>
```

## Views - Escrevendo visualizações regulares do Django usando nosso Serializer:

Vamos ver como podemos escrever algumas visualizações de API usando nossa nova classe Serializer. 

+ Edite o arquivo consumo/views.py e adicione o seguinte:

```python
from django.shortcuts import render
import openpyxl
from .models import Pessoas

def index(request):
    if "GET" == request.method:
        return render(request, 'consumo/index.html', {})
    
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
       
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'consumo/index.html', {"excel_data":excel_data})
```

## Foi criado dentro do app consumo, um arquivo chamado urls.py:

Usando o seguinte código:
```python
from django.urls import path

from .views import index

app_name = "consumo"

urlpatterns = [
    path('', index, name='index'),
]
```

## Foi criado dentro do app consumo, um arquivo chamado viewsets.py:

Usando o seguinte código:
```python
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
        ```

## Urls - Precisamos conectar essas visualizações:

### Suas URLs no Django REST!

Queremos que  http://127.0.0.1:8000/ seja a página inicial da nossa consumo API e exiba uma as urls que configuramos anteriormente.

Abra o arquivo consumo/core/urls.py no seu editor e veja o que aparece:


```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from consumo import views
from consumo.viewsets import PessoasSexosViewSet

router = routers.DefaultRouter()
#router.register(r'meeren', PessoasViewSet, basename='Pessoas')
router.register(r'sexo', PessoasSexosViewSet, basename='PessoasSexos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('consumo.urls')),
    #path('export/', views.export),
    path('pessoas/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

+ Vamos startar o servidor web

```python
python manage.py runserver #startando o servidor
```

```python
 http://127.0.0.1:8000/
```

## E por fim o meu settings.py, ficou desse forma:
```python
"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m4mgph*u*bk%e)p71lbq9!m#ptj*9#7%dv^0&81_o3oio7tpuz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'consumo',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

DATE_FORMAT = "%d/%m/%Y"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```


Agora podemos vizualizar a página de API Root do nosso consumo api.
