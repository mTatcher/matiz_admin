from django.urls import path

from news.views import client

urlpatterns = [
    path("api_client/", client)
]
