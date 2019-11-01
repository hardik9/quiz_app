from django.shortcuts import render
from .forms import UserRegistrationForm


def quiz_home(request):
    context = {
        'user': request.user,
    }
    return render(request, 'users/quiz_home.html',  context=context)


def user_register(request):
    form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context=context)
