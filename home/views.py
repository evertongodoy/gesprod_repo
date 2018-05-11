from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.

def inicio(request):
    return render(request, 'home.html')


def meu_logout(request):
    logout(request)
    return redirect(inicio)

# Everton Godoy - 10/05/2018
# Se o usuario estiver logado, mostrar botao do Sistema
#def sistema(request):
#    pass




