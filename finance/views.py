from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import Budget

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form':form})
    
def login_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') #redirect back to homepage
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/login.html', {'form':form})
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def budget_dashboard(request):
    user_budget = Budget.objects.filter(user=request.user).last
    return render(request, 'budget_dashboard.html', {'budget':user_budget})

