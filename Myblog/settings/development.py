"""
Django settings for Myblog project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .base import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r$%66%a14$r#8@^&vgh&jb=t#9(k14(5jm*7q-viy_qqf7qo=)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
#
# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.sqlite3',
#         'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'mysite_db',
        'USER':'lee',
        'PASSWORD':'lee123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '2964958138@qq.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_SUBJECT_PREFIX = '【樂壹李的博客】'
EMAIL_USE_TLS = True
