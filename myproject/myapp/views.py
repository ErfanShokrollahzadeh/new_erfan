from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Your account has been created successfully.')
            return redirect('myapp:root')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='myapp:login')
def root_view(request):
    context = {
        'user': request.user,
        'messages': messages.get_messages(request)
    }
    return render(request, 'root.html', context)

@login_required(login_url='myapp:login')
def route_view(request):
    context = {
        'user': request.user,
        'messages': messages.get_messages(request)
    }
    return render(request, 'route.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myapp:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='myapp:login')
def dashboard_view(request):
    context = {
        'user': request.user,
        'messages': messages.get_messages(request)
    }
    return render(request, 'dashboard.html', context)
