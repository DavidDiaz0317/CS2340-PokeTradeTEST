from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required
from Collection.utils import generateRandomPokemon


def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            role = request.POST.get('role')
            print(f"Role: {role}")

            if role == 'user':
                user.is_active = True
                user.is_superuser = False
                user.is_staff = False
            if role == 'admin':
                user.is_active = True
                user.is_staff = True
                user.is_superuser = True
            user.save()

            for i in range(4):
                generateRandomPokemon(user)

            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})


def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            template_data['error'] = "The username or password you entered is incorrect."
            return render(request, 'accounts/login.html', {'template_data': template_data})
        elif user.is_staff or user.is_superuser:
            auth_login(request, user)
            return redirect('admin:index')
        else:
            auth_login(request, user)
            return redirect('Collection.index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts.login')