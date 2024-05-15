from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator





import random
import string


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
    extra_context = {'title': 'Authenticted'}


def logout_view(request):
    form = RegisterUserForm()

    if request.method == 'POST':

        logout(request)

    return render(request, 'users/logout.html', {})



# def generate_random_string(length=6):
#     letters_and_digits = string.ascii_letters + string.digits
#     return ''.join(random.choice(letters_and_digits) for i in range(length))

# # Функция для отправки письма с кодом подтверждения
# def send_confirmation_email(request, user):
#     # Генерируем код подтверждения
#     confirmation_code = generate_random_string()
#     user.confirmation_code = confirmation_code
#     user.save()

#     # Формируем ссылку для подтверждения
#     current_site = get_current_site(request)
#     mail_subject = 'Подтверждение регистрации'
#     message = render_to_string('users/confirmation_email.html', {
#         'user': user,
#         'domain': current_site.domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': default_token_generator.make_token(user),
#     })
#     user.email_user(mail_subject, message)

# # В представлении для регистрации добавляем отправку письма с кодом подтверждения
def register(request):
    form = RegisterUserForm() 

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
    else:
        form = RegisterUserForm()

    return render(request, 'users/register.html', {'form': form})




