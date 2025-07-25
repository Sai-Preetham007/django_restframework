from django.urls import path
from student_api import views

urlpatterns = [
    path("students/", views.Students_List.as_view()),
    path("students/<int:pk>", views.Student_by_id.as_view()),
    path("institute/", views.Institute_List_Create.as_view()),
    path("institute-update/<int:pk>", views.Institute_Retrieve_Update.as_view()),
    path("institute-destroy/<int:pk>", views.Institute_Destroy.as_view())
]