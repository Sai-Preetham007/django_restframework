from django.urls import path
from home import views

urlpatterns = [
    path("index/", views.index),
    path("api/person/", views.person),
]