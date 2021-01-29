from django.urls import path
from .views import home_view, student_add, student_list


urlpatterns = [
    path("", home_view, name="Home"),
    path("add/", student_add, name="add"),
    path("list/", student_list, name="list")
]