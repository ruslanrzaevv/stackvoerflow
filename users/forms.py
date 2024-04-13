from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import User


class ChangeProfileForm(UserChangeForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            'link',
        )


