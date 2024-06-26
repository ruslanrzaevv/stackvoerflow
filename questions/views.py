from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from questions.models import Question, Answer
from django.db.models import Q
from questions.forms import AddQuestionForm, AddAnswerForm
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model()

# @login_required
def index(request):
    questions = Question.objects.all()


    
    if request.POST.get('q'):
        search = request.POST.get('q', '')

        questions = Question.objects.filter(
            Q(title__icontains=search)
        )


    context = {
        'questions': questions,
    }

    return render(request, 'questions/index.html', context)

def quest_detail(request, question_slug):
    question = get_object_or_404(Question, slug=question_slug)
    answers = Answer.objects.all()
         
    form = AddAnswerForm()
    
    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }

    return render(request, 'questions/question_detail.html', context)


def questions_from_tag(request, tag_id):
    questions = Question.objects.filter(tag=tag_id)

    context = {
        'questions': questions,
    }

    return render(request, 'questions/index.html', context)


@login_required
def add_question(request):
    form = AddQuestionForm()

    if request.method == 'POST':
        form = AddQuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'questions/add_question.html', context)


def add_answer(request,  question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AddAnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question  
            answer.save()   

    return redirect('quest_detail', question.slug)


def tags(request):
    tags = Question.tag.all()

    return render(request, 'questions/tags.html', {'tag':tags})


def users_l(request):

    
    user = User.objects.all()
    return render(request, 'questions/user.html' , {'user':user})


