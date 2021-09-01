from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('add/', views.addEmployee, name="add_employee"),
    path('view/', views.viewEmployee, name="view_employee"),
    path('update/<str:employee_id>', views.updateEmployee, name="update_employee"),
    path('delete/<int:employee_id>', views.deleteEmployee, name="delete_employee"),
    path('signin/', views.signin, name="signin"), 
    path('signout/',views.signout, name="signout"),
]
