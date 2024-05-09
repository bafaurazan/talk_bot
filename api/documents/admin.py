"""which models should be shown on the admin site"""

from django.contrib import admin
from .models import Document

admin.site.register(Document)
