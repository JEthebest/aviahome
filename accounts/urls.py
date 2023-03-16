from django.contrib import admin
from django.urls import path, include

from accounts import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('', views.login_user, name='user-login'),
    path('logout/', LogoutView.as_view(next_page="main-page"), name="user-logout"),
    path('<int:pk>/', views.user_profile, name="user-profile"),
    path('signup/', views.signup, name="user-create"),
    path('<int:pk>/update/', views.user_update, name="user-update"),
    path('users/', views.main_page, name='main-page'),
]

