from django.db import models


class Document(models.Model):
    command = models.TextField()
    request_path = models.TextField()
    documentation = models.TextField(default="No documentation")
