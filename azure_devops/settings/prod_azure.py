import os
from .prod import *

# DEBUG = False

if 'IGNORE_DJANGO_STORAGES' not in os.environ:
    INSTALLED_APPS += ['storages']

    STATICFILES_STORAGE = 'azure_devops.azure_storages.StaticAzureStorage'
    DEFAULT_FILE_STORAGE = 'azure_devops.azure_storages.MediaAzureStorage'

    AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')

