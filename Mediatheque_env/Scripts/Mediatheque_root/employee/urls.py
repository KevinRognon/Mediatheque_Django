from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee, name="employee"),
    path('employees/show-members/', views.show_members, name="show_members")
]

