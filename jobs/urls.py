from django.urls import path
from .views import list_jobs, detail_job

app_name = "jobs"

urlpatterns = [
    path('', list_jobs, name="list"),
    path('<int:pk>/', detail_job, name='details'),
]
