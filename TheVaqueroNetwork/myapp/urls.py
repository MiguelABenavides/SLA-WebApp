from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_or_create_user, name='login_or_create'),
    path('dashboard/', views.dashboard, name='dashboard'),

]