# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sholyh1f(ezsnst+#4-+mpraws0*c6077%71g0e9h@a7klb-kc'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}