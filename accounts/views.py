from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from accounts.models import student, group
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully")
            return redirect('login')
        else:
            context['form'] = form

    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, "accounts/register.html", context)


def login_view(request):
    context = {}

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:

            context['form'] = form

    else:
        form = LoginForm()
        context['form'] = form
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "yyou have successfullyy logged out....")
    return redirect('login')

def display_info(request):
    current_user = request.user
    gr_id = current_user.group_id

    context = {'current': current_user, 'gr_id': gr_id,}
    return render(request, "accounts/display_profile.html", context)

@login_required(login_url="/accounts/login")
def edit_profile(request, id):
    context = {}
    lu = student.objects.get(id=id)
    context['current_user'] = request.user
    context['gr_id'] = request.user.group_id

    form = RegistrationForm(instance=lu)
    if request.POST:
        form = RegistrationForm(request.POST, instance=lu)
        if form.is_valid():
            form.save()
            messages.success(request, "account updated successfully")
            return redirect('dashboard')
        else:
            context['form'] = form

    else:

        context['form'] = form
    return render(request, "accounts/edit_profile.html", context)
