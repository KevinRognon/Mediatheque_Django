from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('/show_medias_member'), name="member"),
    path('show_medias_member', views.show_medias_member, name="show_medias_member")
]