from django.urls import path
from . import views

from users.views import profile, edit_profile, logout_view, register


urlpatterns = [
    path('login/', views.loginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/<slug:username>/', profile, name='profile'), 
    path('profile/edit/<slug:username>/', edit_profile, name='edit_profile'),
    path('confirmation_sent/', views.confirmation_sent, name='confirmation_sent'),

]