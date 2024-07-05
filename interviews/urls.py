from django.urls import path
from .views import create, details

app_name = "interviews"

urlpatterns = [
    path("create/<int:job_pk>/", create, name="create"),
    path("<uuid:uuid>/", details, name="details")
]