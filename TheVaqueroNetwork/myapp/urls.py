from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_or_create_user, name='login_or_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/activities/', views.activities, name='activities'),
    path('dashboard/activities/add/', views.add_task, name='add_task'),
    path('dashboard/calendar/', views.calendar, name='calendar'),
    path('dashboard/bulletin/', views.bulletin_board, name='bulletin_board'),
    path('dashboard/emergency/', views.emergency_contacts, name='emergency_contacts'),
]