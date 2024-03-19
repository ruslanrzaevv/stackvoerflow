from django import forms
from tinymce.widgets import TinyMCE

from questions.models import Question, Answer

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body', 'tag',)
        widgets = {
            'body': TinyMCE(attrs={'cols': 50, 'rows': 30,}),
        }



class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)