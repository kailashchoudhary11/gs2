from django.urls import path
from .views import student_details, create_student
app_name = "api"

urlpatterns = [
    path("<int:id>/", student_details, name="student_details"),
    path("create", create_student, name="create"),
]
