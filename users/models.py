from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class User(AbstractUser):
    image = models.ImageField(default='profile.wepb', upload_to='users_images', blank=True,)
    email_confirmated = models.BooleanField(default=False)
    link = models.URLField(blank=True)  