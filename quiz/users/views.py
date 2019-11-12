from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm



def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
        'form_errors': list(form.errors.values()),
    }
    return render(request, 'users/register.html', context=context)
