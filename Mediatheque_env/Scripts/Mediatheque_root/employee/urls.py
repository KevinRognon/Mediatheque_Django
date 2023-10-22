from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('/employees'), name="employee"),
    path('employees/', views.employee, name="employee"),
    path('employees/show-members/', views.show_members, name="show_members"),
    path('employees/show-medias/', views.show_medias, name="show_medias"),
    path('employees/create-member/', views.create_member, name="create_member"),
    path('employees/detail/<int:id>', views.show_details, name="show_details"),
    path('employees/delete-member/<int:member_id>/', views.delete_member, name="delete_member"),
    path('employees/add-media', views.add_media, name="add_media")
]

