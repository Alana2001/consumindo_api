from django.urls import path

from .views import index

app_name = "consumo"

urlpatterns = [
    path('', index, name='index'),
]