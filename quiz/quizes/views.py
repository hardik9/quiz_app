from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def new_quiz(request):
    
    context = {
        'user': request.user,
    }
    return render(request, 'quizes/quiz.html', context=context)


@login_required
def quiz_home(request):
    context = {
        'user': request.user,
    }
    return render(request, 'quizes/quiz_home.html',  context=context)

@login_required
def add_q(request):
    context = {
        'user': request.user,
    }
    return render(request, 'quizes/add_q.html', context=context)
