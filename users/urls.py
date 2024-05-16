from django.urls import path
from . import views


from users.views import profile, edit_profile, logout_view


urlpatterns = [
    path('login/', views.loginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<slug:username>/', views.profile, name='profile'),
    path('profile/edit/<slug:username>/', views.edit_profile, name='edit_profile'),
    path('register/',views.RegisterUser.as_view() , name='register'),

]