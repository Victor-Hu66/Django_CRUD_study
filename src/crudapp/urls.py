from django.urls import path
from .views import home_view, student_add, student_list, student_detail, student_delete


urlpatterns = [
    path("", home_view, name="Home"),
    path("add/", student_add, name="add"),
    path("list/", student_list, name="list"),
    path("<int:id>", student_detail, name="detail"),
    path("<int:id>/delete", student_delete, name="delete")
]