from django.shortcuts import render


def quiz_home(request):
    context = {
        'user': request.user,
    }
    return render(request, 'users/quiz_home.html',  context=context)
