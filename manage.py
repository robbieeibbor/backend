import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emissions_django_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "this message was generated: Couldn't import Django"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
