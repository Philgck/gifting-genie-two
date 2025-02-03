from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.planner_home, name='planner_home'),
    path('create/', views.create_plan, name='create_plan'),
    path('edit/<int:plan_id>/', views.edit_plan, name='edit_plan'),
    path('delete/<int:plan_id>/', views.delete_plan, name='delete_plan'),
]