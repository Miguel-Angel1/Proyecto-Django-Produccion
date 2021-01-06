"""
Sección 4:Sección 4: Entorno de trabajo optimo en Django
4.5: Urls de aplicaciones
-> Importación de las librerias re_path e inlcude
-> Incluir las url de la aplicacion Departamento:
   re_path('', include('Applications.Departamento.urls')),

"""
from django.contrib import admin
from django.urls import path, re_path, include

#11.14 Importar Librerias para Multimedia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('Applications.Departamento.urls')),
    # 5.2.5 Busqueda de urls en la app Home_Pruebas
    re_path('', include('Applications.Home_Pruebas.urls')),
    re_path('', include('Applications.Empleado.urls')),
#11.14 generar URLs staticas para las imagenes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
