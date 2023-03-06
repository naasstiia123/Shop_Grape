from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm

# Create your views here.
def login_view(request):
    """
    Shows page with form to log in. Log  in on the site.
    :return:redirect on main page of the site

    """
    form = LoginForm(request.POST or None)
    next_get = request.GET.get('next')

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')

        return redirect(next_get or next_post or '/')

    return render(request, 'login.html', context={'form': form})

def logout_view(request):
    """
    Log out from the site.
    :return:redirect on main page of the site

    """
    logout(request)
    return redirect('/')

def registration_view(request):
    """
    Shows page with form to registration. Registration on the site.
    :return:redirect on main page of the site

    """
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        user = RegistrationForm(request.POST).save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('/')

    return render(request, 'registration.html', context={'form': form})
