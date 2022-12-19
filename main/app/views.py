from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login, authenticate, logout as logout 
from django.contrib import messages
from .forms import*
from .models import *
from django.http import HttpResponse

def index(request):
    context = {

    }

    return render(request, 'index.html', context)


#Sign_up
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Üstünlikli amala aşyryldy' + user)
                return redirect('/')
            else:
                messages.info(request, 'e-mail pocta öň registrasiýa edilen')
        return render(request, 'sign_up.html', {'form': form})



#Sign_in
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            email = authenticate(email=email, password=password)

            if email is not None:
                login(request,email)
                return redirect('index')
            else:
                messages.info(request, 'Ulanyjy email poctasy ýa-da paroly nädogry')
        context = {}
        return render(request, 'sign_in.html', context)
