from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddTrueFalseForm


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
    if request.method == 'POST':
        form = AddTrueFalseForm(request.POST)

        if form.is_valid():
            form.save()
            redirect('add-q')
    else:
        form = AddTrueFalseForm()

    context = {
        'user': request.user,
        'form': form,
        'form_errors': list(form.errors.values())
    }
    return render(request, 'quizes/add_q.html', context=context)
