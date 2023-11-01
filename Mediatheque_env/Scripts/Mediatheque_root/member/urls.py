from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('/show_medias'), name="member"),
    path('show_medias', views.show_medias, name="show_medias")
]