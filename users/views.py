from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import User

from users.forms import ChangeProfileForm, LoginUserForm
from questions.models import Question, Answer
from users.models import User


def edit_profile(request, username):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect('profile', request.user.username)
    else:
        form = ChangeProfileForm(instance=request.user)

    context = {
        'form': form,
        'questions':questions,
    }
    
    return render(request, 'users/edit_profile.html', context)


def profile(request, username):

    user = request.user

    questions = Question.objects.all()
    answers = Answer.objects.filter(user=user)
    

    context = {
        'questions': questions,
        'answers':answers,
        'user':user
    }

    return render(request, 'users/profile.html', context)

class loginUser(LoginView):

    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authenticted'}

    
