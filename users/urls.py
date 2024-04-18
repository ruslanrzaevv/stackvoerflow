from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

from users.views import profile, edit_profile


urlpatterns = [
    path('login/', views.loginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<slug:username>/', profile, name='profile'), 
    path('profile/edit/<slug:username>/', edit_profile, name='edit_profile'),
    
]
