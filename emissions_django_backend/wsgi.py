import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emissions_django_backend.settings')

application = get_wsgi_application()
