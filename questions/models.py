from django.db import models
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField
from tinymce.models import HTMLField
from taggit.managers import TaggableManager


User = get_user_model()


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False)
    body = HTMLField(blank=False)
    tag = TaggableManager()
    closed = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = HTMLField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.answer


