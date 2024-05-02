"""Models structure"""

from django.db import models


class Document(models.Model):
    """Document model structure"""

    command: str = models.TextField()
    request_path: str = models.TextField()
    documentation: str = models.TextField(default="No documentation")
