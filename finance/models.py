from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income_level = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
    spending_habits = models.TextField(null=True, blank=True)
    goals = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 

class Investment(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE) 
    portfolio_value = models.DecimalField(max_digits=12, decimal_places=2)
    risk_level =  models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_progress = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
