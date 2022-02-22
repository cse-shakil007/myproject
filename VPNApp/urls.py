from django.urls import path
from . import views



urlpatterns = [
    path("fileDetails/", views.FileDetailsAPIView.as_view()),
    path("appDetails/", views.AppDetailsAPIView.as_view()),
]