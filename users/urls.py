from django.urls import path

from users.views import profile

urlpatterns = [
    path('profile/<slug:username>/', profile, name='profile'), 
]