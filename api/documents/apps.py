"""Defining app"""

from django.apps import AppConfig


class DocumentConfig(AppConfig):
    """App specification"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "documents"
