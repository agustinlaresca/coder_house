INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',         # App para el blog
    'accounts',     # App para cuentas y perfiles de usuario
]
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'