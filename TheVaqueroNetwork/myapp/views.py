from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
import calendar as cal_module
from .models import Task

def home(request):
    return render(request, 'home.html')



def login_or_create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'home.html', {'error': 'Username and Password cannot be empty.'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            welcome = messages.success(request, f"Welcome back, {username}!")
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

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def activities(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'activities.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if not title:
            messages.error(request, 'Task title is required.')
            return render(request, 'add_task.html')
        Task.objects.create(user=request.user, title=title, description=description)
        messages.success(request, 'Task added successfully!')
        return redirect('activities')
    return render(request, 'add_task.html')


@login_required
def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')
        return redirect('activities')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        if not title:
            messages.error(request, 'Task title is required.')
            return render(request, 'edit_task.html', {'task': task})
        task.title = title
        task.description = description
        task.completed = completed
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('activities')
    return render(request, 'edit_task.html', {'task': task})

@login_required
def calendar(request):
    today = datetime.date.today()

    cal = cal_module.HTMLCalendar().formatmonth(today.year, today.month)

    context = {
        'current_date': today.strftime("%A, %B %d, %Y"),
        'calendar': cal
    }
    return render(request, 'calendar.html', context)

@login_required
def bulletin_board(request):
    return render(request, 'bulletin_board.html')

@login_required
def emergency_contacts(request):
    return render(request, 'emergency_contacts.html')


@login_required
def log_out(request):
    logout(request)
    return redirect('home')


@login_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('activities')
