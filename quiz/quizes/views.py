from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def new_quiz(request):
    
    context = {
        'user': request.user,
    }
    return render(request, 'quizes/quiz.html', context=context)