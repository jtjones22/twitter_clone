from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from authentication.forms import LoginForm, SignupForm
from twitteruser.models import Profile

# Create your views here.


def loginview(request):
    html = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    context = {
        'form': form
        }
    return render(request, html, context)


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signupview(request):
    html = 'signup.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Profile.objects.create_user(
                email=data['email'],
                username=data['username'],
                password=data['password'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    context = {'form': form}
    return render(request, html, context)