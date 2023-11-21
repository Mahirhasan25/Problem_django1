from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account has been registered')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'loging.html')

def userlogin(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('login')

def passwordreset(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(user= request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            form = PasswordChangeForm(user= request.user)
        return render(request, 'passwordreset.html', {'form': form})
    else:
        return redirect('login')
    
def passwordreset2(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(user= request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            form = SetPasswordForm(user= request.user)
        return render(request, 'passwordreset.html', {'form': form})
    else:
        return redirect('login')


