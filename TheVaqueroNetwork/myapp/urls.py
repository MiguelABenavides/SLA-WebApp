from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_or_create_user, name='login_or_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/activities/', views.activities, name='activities'),
    path('dashboard/activities/add/', views.add_task, name='add_task'),
    path('dashboard/activities/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('dashboard/activities/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('dashboard/calendar/', views.calendar, name='calendar'),
    path('dashboard/bulletin/', views.bulletin_board, name='bulletin_board'),
    path('dashboard/emergency/', views.emergency_contacts, name='emergency_contacts'),
    path('logout/', views.log_out, name='log_out'),
]