from django.urls import path
from questions.views import index, quest_detail, add_question, questions_from_tag, add_answer, tags, users_l

urlpatterns = [
    path('', index, name='index'), 
    path('tags/<int:tag_id>/', questions_from_tag, name='tag_detail'),
    path('tags/',tags, name='tags'),
    path('question/<slug:question_slug>/', quest_detail, name='quest_detail'),
    path('add_question/', add_question, name='add_question'),
    path('add_answer/<int:question_id>/', add_answer, name='add_answer'),
    path('user/', users_l, name='user'),
    ]


