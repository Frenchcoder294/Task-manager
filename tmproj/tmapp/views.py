from django.shortcuts import render, redirect
from django.http import request
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
# Create your views here.

def home(request):
    return render(request, 'home.html')
@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
        return render(request, 'create_task.html', {'form':form})
@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    user = request.user
    if not user.is_authenticated:
        messages.error(request, 'you have to login to see the tasks')
    return render(request, 'task_list.html', {'tasks':tasks})

def edit_task(request, task_id):
    task = Task.objects.get(id = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance = task)
        return render(request, 'edit_task.html', {'form':form, 'task':task})

def remove_task(request, task_id):
    task = Task.objects.get(id = task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'remove_task.html', {'task':task})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email already in use')
                return redirect('register')
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            messages.success(request, 'user creation successful')
            return redirect('login')
        messages.error(request, 'passwords you entered are not the same')
        return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is invalid')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')