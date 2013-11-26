# -*- coding: utf-8 -*-

"""
Created on 12/12/2011
@author: romuloigor@solidit.com.br 
"""

# Django settings for myproject project.
import os, sys, socket

# Recomendations using Virtualenv.
# yes | sudo apt-get install python-pip
# yes | sudo pip install virtualenv
# yes | sudo pip install virtualenvwrapper
# source /usr/local/bin/virtualenvwrapper.sh
# mkvirtualenv myproject

# #***** INI PIL *****
# # Instalando Python Image Library.
# yes | sudo apt-get install libjpeg-dev
# yes | sudo apt-get install libfreetype6
# yes | sudo apt-get install libfreetype6-dev
# yes | sudo apt-get install zlib1g-dev
# if [ ! -L "/usr/lib/libjpeg.so" ]; then
#    sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
# fi
# if [ ! -L "/usr/lib/libfreetype.so" ]; then
#    sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
# fi
# if [ ! -L "/usr/lib/libz.so" ]; then
#    sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
# fi
# yes | sudo pip install PIL
# #***** FIM PIL *****

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# 
ENABLE_SESSIONS_TIMEOUT = True
SESSION_TIMEOUT = 1 * 60 #segundos
SESSION_SECURITY_WARN_AFTER = SESSION_TIMEOUT/3 #segundos

#
ENABLE_SIMULTANEOUS_SESSIONS_LOGINS = True

# 
ENABLE_CLICK_TRACKING = True

# Root Dir e essencial para as demais variaveis do projeto. 
ROOTDIR = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        ## Enable SQLite database.
        #***************************************
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/myproject.db' % ROOTDIR,  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.

        ## Enable Amazon RDS for MySQL database.
        # yes | sudo apt-get install python-pip
        # yes | sudo easy_install -U distribute
        # yes | sudo apt-get install libmysqlclient-dev
        # yes | sudo apt-get install python2.7-dev
        # yes | sudo pip install MySQL-python
        #***************************************
        # 'ENGINE": 'django.db.backends.mysql',
        # 'NAME": 'myproject',
        # 'USER": 'myproject',
        # 'PASSWORD": '12qwaszx',
        # 'HOST': 'myproject.cb7madzrmw4h.sa-east-1.rds.amazonaws.com',
        # 'PORT': '3306',

        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
        #python manage.py createcachetable django_cache

        #  Enable Amazon Elastic Cache
        # yes | sudo apt-get install memcached
        # yes | sudo apt-get install python-memcache
        #***************************************
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': 'myproject.dzoo5z.cfg.sae1.cache.amazonaws.com:11211',

        # Enable Amazon DynamoDB for Click Tracking
        # yes | sudo pip install dynamodb-mapper
        #***************************************
        'CLICK_TABLE': 'click',
        'READ_UNITS': 10,
        'WRITE_UNITS' : 10,
        
        # Set AWS Region
        'REGION' : 'us-east-1',
    }
}

CACHES = DATABASES

#
#
#yes | sudo pip install django-ses
# AWS_SES_REGION_NAME = DATABASES["default"]["REGION"]
# AWS_SES_REGION_ENDPOINT = "email-smtp.us-east-1.amazonaws.com"
#AWS_SES_ACCESS_KEY_ID = "AKIAJ22BNYZQGK7HFCQQ"
#AWS_SES_SECRET_ACCESS_KEY = "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"

#
#yes | sudo pip install django-smtp-ssl
EMAIL_BACKEND = "django_smtp_ssl.SSLEmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
EMAIL_HOST_USER = "XXXXXXXXXXXXXXXXXXX"
EMAIL_HOST_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
EMAIL_PORT = 465

#http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
# pip install django-storage

# Credenciais
AWS_STORAGE_BUCKET_NAME = "myproject"
AWS_ACCESS_KEY_ID = "XXXXXXXXXXXXXXXXXXX"
AWS_SECRET_ACCESS_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Upload
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Collectstatic
STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"
AWS_S3_SECURE_URLS = False

#Se usar CloudFront
#AWS_S3_CUSTOM_DOMAIN = "d2jfhjcqz2ztph.cloudfront.net"

#AWS_S3_CUSTOM_DOMAIN = '%s.s3-website-us-west-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = '127.0.0.1/static_myproject'

# http://dynamodb-mapper.readthedocs.org/en/latest/
# Amazon DynamoDB
# yes | sudo pip install dynamodb-mapper
# yes | sudo pip install pytz

if ENABLE_CLICK_TRACKING:
    def create_dynamoDB():
        from dynamodb_mapper.model import ConnectionBorg
        from portal.models_norel.click import Click
        from django.conf import settings

        conn = ConnectionBorg()
        conn.set_region( '%s' % settings.DATABASES["default"]["REGION"] ) 

        obj_click = Click()
        try:
            conn.create_table(obj_click, read_units=settings.DATABASES["default"]["READ_UNITS"], write_units=settings.DATABASES["default"]["WRITE_UNITS"], wait_for_active=False)
        except Exception, args:
            print args
        
        create_dynamoDB()

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "America/Sao_Paulo"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'
DATABASE_OPTIONS = {"charset": "utf8"} 
DEFAULT_CHARSET = "utf-8"

LANGUAGES = (
    ('pt-br', u'Portugues (Brasil)'),
)

# Install PT-BR Language Pack
# yes | sudo apt-get install language-pack-pt
# sudo locale-gen pt_BR.UTF-8

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '%s/media' % ROOTDIR

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://%s/media/' % AWS_S3_CUSTOM_DOMAIN

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = '%s/static' % ROOTDIR
STATIC_ROOT = '/Library/WebServer/Documents/static_myproject/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#STATIC_URL = 'http://%s/static/' % AWS_S3_CUSTOM_DOMAIN
STATIC_URL = 'http://%s/static_myproject/' % AWS_S3_CUSTOM_DOMAIN

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '52=10j+mpubdvr*wm1vz#pf_vwki8&3%2!&*61!3y1-ye=_j=1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.transaction.TransactionMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    
    "portal.middleware.multilogin_restrict.MultiLoginRestrictMiddleware",
    "portal.middleware.session_expired.SessionExpiredMiddleware",

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

ROOT_URLCONF = 'myproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myproject.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    #yes | sudo pip install django-storages
    'storages',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'portal',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
