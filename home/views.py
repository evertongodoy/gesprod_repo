from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.

def inicio(request):
    return render(request, 'home.html')


def meu_logout(request):
    logout(request)
    return redirect(inicio)



