from django.shortcuts import render
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm
    
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")
