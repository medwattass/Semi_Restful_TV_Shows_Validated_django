"""
WSGI config for Semi_Restful_TV_Shows_Validated project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Semi_Restful_TV_Shows_Validated.settings')

application = get_wsgi_application()
