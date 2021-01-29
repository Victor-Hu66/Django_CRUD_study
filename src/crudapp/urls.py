from django.urls import path
from .views import home_view, student_add


urlpatterns = [
    path("", home_view, name="Home"),
    path("add/", student_add, name="add")
]