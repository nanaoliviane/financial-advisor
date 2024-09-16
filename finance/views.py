from django.shortcuts import render
from .models import Budget

def budget_dashboard(request):
    user_budget = Budget.objects.filter(user=request.user).last
    return render(request, 'budget_dashboard.html', {'budget':user_budget})

# Create your views here.
