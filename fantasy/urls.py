from django.urls import path
from . import views

urlpatterns = [
    path("my-team/", views.my_team, name="my_team"),
]
