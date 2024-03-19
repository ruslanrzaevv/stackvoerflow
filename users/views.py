from django.shortcuts import render, redirect

from users.forms import ChangeProfileForm
from questions.models import Question


def profile(request, username):
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
    
    return render(request, 'users/profile.html', context)