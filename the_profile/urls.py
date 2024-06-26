from django.urls import path
from . import views 

from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
app_name = 'Profile'
urlpatterns = [
    path('',views.Profile.as_view(),name='profile'),
    path('login/',auth_views.LoginView.as_view(next_page='Profile:profile',redirect_authenticated_user=True),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='Profile:login'),name='logout'),
]