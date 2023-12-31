from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from .backends import EmailBackend

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            staff_id = form.cleaned_data['staff_id']
            password = form.cleaned_data['password']
            user = EmailBackend().authenticate(request, username=staff_id, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your home page

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})
