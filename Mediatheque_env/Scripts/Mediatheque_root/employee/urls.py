from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('main/'), name="employee"),
    path('main/', views.employee, name="employee"),
    path('show-members/', views.show_members, name="show_members"),
    path('show-medias/', views.show_medias, name="show_medias"),
    path('create-member/', views.create_member, name="create_member"),
    path('media-detail/<str:media_type>/<int:media_id>/', views.media_detail, name="media_detail"),
    path('delete-member/<int:member_id>/', views.delete_member, name="delete_member"),
    path('add-media', views.add_media, name="add_media")
]

