from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import User
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import  reverse_lazy


from users.forms import ChangeProfileForm, LoginUserForm, RegisterUserForm
from questions.models import Question, Answer
from users.models import User


User = get_user_model()



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
    extra_context = {'title': 'Authenticated'}


def logout_view(request):
    form = RegisterUserForm()

    if request.method == 'POST':

        logout(request)

    return render(request, 'users/logout.html', {})

# def register(request):

#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)

#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password',])
#             user.save()
#             # return render(request, 'users/reg_done.html')
#             return redirect('index')
#         print('hello')
            
#     else:
#         form = RegisterUserForm()

#     return render(srequest, 'users/register.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('index')
    def hello():
        return print('hello')




