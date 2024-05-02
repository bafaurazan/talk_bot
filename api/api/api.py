"""All routers are connected here"""

from ninja import NinjaAPI
from django.urls import path

api = NinjaAPI()

api.add_router("/", "documents.views.router")

urlpatterns = [
    path("api/", api.urls),
]
