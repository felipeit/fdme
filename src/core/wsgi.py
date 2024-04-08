# """
# WSGI config for mysite project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# from whitenoise.django import DjangoWhiteNoise


# application = Cling(get_wsgi_application())

# application = DjangoWhiteNoise(application)
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()