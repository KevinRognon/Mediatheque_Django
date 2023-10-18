from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee, name="employee"),
    path('employees/show-members/', views.show_members, name="show_members"),
    path('employees/show-medias/', views.show_medias, name="show_medias"),
    path('employees/create-member/', views.create_member, name="create_member"),
    path('employees/delete-member/<int:member_id>/', views.delete_member, name="delete_member")
]

