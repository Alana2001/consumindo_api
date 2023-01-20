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