"""
Sección 4: Entorno de trabajo optimo en Django
4.1 Organizando el archivo settings

    from .base import *
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['142.93.203.184']
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'mysql_cymysql',
        'NAME': 'dbempleado',
        'USER': 'proyecto',
        'PASSWORD': 'admin1234H',
        'HOST': '142.93.203.184',
        'PORT': '3306',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
# 10.2 Integración de archivos Estáticosx4
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

#11.14 Archivos Multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
