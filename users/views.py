from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import User
from django.core.mail import send_mail


from users.forms import ChangeProfileForm, LoginUserForm, RegisterUserForm
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


def logout_view(request):
    form = RegisterUserForm()

    if request.method == 'POST':

        logout(request)

    return render(request, 'users/logout.html', {})



def register(request):
    form = RegisterUserForm() 

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            send_mail(
                'Потверждение регистрации',
                'Код для потверждения: 1234567',
                'azbergen74@gmail.com',
                [user.email],
                fail_silently=False,
            )


            return redirect('confirmation_sent')
    else:
        form = RegisterUserForm()

    return render(request, 'users/register.html', {'form': form})


def confirmation_sent(request):
    if request.method == 'POST':
        confirmation_code = request.POST.get('confirmation_code')
        if confirmation_code == '123456':  
            return redirect('login')  
        else:
            return render(request, 'users/confirmation_sent.html', {'error': 'Неверный код подтверждения'})
    return render(request, 'users/confirmation_sent.html')
