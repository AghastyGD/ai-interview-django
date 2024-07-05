from django.urls import path
from .views import create, details, create_message

app_name = "interviews"

urlpatterns = [
    path("create/<int:job_pk>", create, name="create"),
    path("<uuid:uuid>/", details, name="details"),
    path("<uuid:chat_uuid>/create-message", create_message, name="create_message")
]