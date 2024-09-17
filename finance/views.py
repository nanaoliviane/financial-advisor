from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import Budget
from .models import Goal
from .models import Investment
from .models import UserProfile

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

@login_required
def goal_list_view(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goal/goals.html', {'goals': goals})

@login_required
def user_profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profile/profile.html', {'profile': profile})

@login_required
def investment_portfolio_view(request):
    investments = Investment.objects.filter(user=request.user)
    return render(request, 'investment/portfolio.html', {'investments': investments})

@login_required
def budget_dashboard_view(request):
    budget = Budget.objects.filter(user=request.user).last()
    return render(request, 'budget/dashboard.html', {'budget': budget})


