from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    ID = models.CharField(max_length = 8, primary_key=True, null=False)
    Name = models.CharField(max_length=100,default="", null=True)
    Age = models.CharField(max_length=100,default="", null=True)

    def __str__(self):
        return self.Emp_ID
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model: User
        fields = ('username','email','password1','password2')

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)