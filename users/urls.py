from django.urls import path

from users.views import profile, edit_profile

app_name = 'users'

urlpatterns = [
    path('profile/<slug:username>/', profile, name='profile'), 
    path('profile/edit/<slug:username>/', edit_profile, name='edit_profile'),
]