from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(username = username, password = password)
            login(request, new_user)
            return redirect('workouts_home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})