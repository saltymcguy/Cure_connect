import os
from .settings import *

DEBUG = False

allowed_hosts = []
for env_name in ('RAILWAY_PUBLIC_DOMAIN', 'RENDER_EXTERNAL_HOSTNAME', 'RAILWAY_STATIC_URL'):
    value = os.environ.get(env_name, '').strip()
    if value:
        value = value.replace('https://', '').replace('http://', '').split('/')[0]
        allowed_hosts.append(value)

allowed_hosts.extend(['localhost', '127.0.0.1', '.railway.app'])
ALLOWED_HOSTS = allowed_hosts

SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-production')

if os.environ.get('DATABASE_URL'):
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME', 'cure_connect'),
            'USER': os.environ.get('DATABASE_USER', 'postgres'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
            'PORT': os.environ.get('DATABASE_PORT', '5432'),
        }
    }

STATIC_ROOT = BASE_DIR / 'staticfiles'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
