from django.contrib import admin
from questions.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'closed', 'created_at', 'updated_at',)
    list_display_links = ('id', 'user')  

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer', 'created_at', 'updated_at',)
    list_display_links = ('id', 'user')
    