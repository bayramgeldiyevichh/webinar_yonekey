from django.shortcuts import render
from .models import *

def index(request):
    context = {

    }

    return render(request, 'index.html', context)


def register(request):

    return render(request, 'login_page.html')
