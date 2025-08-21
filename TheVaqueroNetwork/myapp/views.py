from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def login_or_create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'home.html', {'error': 'Username and Password cannot be empty.'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('dashboard')  # Redirect to a new dashboard page
        else:
            try:
                User.objects.get(username=username)
                return render(request, 'home.html', {'error': 'Invalid username or password.'})
            except User.DoesNotExist:
                new_user = User.objects.create_user(username=username, password=password)
                new_user.save()

                login(request, new_user)
                messages.success(request, "Account created successfully! Welcome!")
                return redirect('dashboard')  # Redirect to the dashboard

    return redirect('home')