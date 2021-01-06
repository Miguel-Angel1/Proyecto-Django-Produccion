# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
"""
Sección: 5.0 Vistas en Django
5.4 Templates en vistas genéricas - Aplicación Home_Pruebas
Modificación del archivo base.py, para tener todos los templates
en una sola carpeta

*Linea Original*
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

*Linea de reemplazo*
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

"""

from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5_anqih&!eey2x53d2yk-f80u5#!l_uaaxw=&b)9740$p%y_8n'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps de terceros

    # Sección 4:
    # 4.4 Instalando un app en Django
    # Debemos indicarle a django que instala las apps que hemos creado
    'ckeditor',
    'Applications.Departamento',
    'Applications.Empleado',

    # Sección 5: Vistas en Django
    # 5.2 Vistas Basadas en Clases – Aplicación Home_Pruebas.
    # Instalación de a aplicación Home_Pruebas
    'Applications.Home_Pruebas',

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

ROOT_URLCONF = 'Primer_Proyecto_Curso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 5.4.1: Agregación de nuestro directorio Templates donde estaran todos nuestros html
        'DIRS': [BASE_DIR.child('Templates')],

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

WSGI_APPLICATION = 'Primer_Proyecto_Curso.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
