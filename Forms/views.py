from django.shortcuts import render, redirect
from .models import Formularios
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    forms= Formularios.objects.filter()
    return render(request, 'home.html', {'forms': forms})

def create_form(request):
    if request.POST:
        Titulo= request.POST.get('titulo')
        pergunta1 = request.POST.get('pergunta1')
        pergunta2 = request.POST.get('pergunta2')
        pergunta3 = request.POST.get('pergunta3')
        pergunta4 = request.POST.get('pergunta4')
        pergunta5 = request.POST.get('pergunta5')
        user=request.user
        form= Formularios.objects.create(Titulo = Titulo, pergunta1=pergunta1,
        pergunta2 = pergunta2, pergunta3 = pergunta3, pergunta4 = pergunta4,
        pergunta5 = pergunta5, Autor = user)
    return render(request, 'Formulario.html')

def logar(request):
    return render(request, 'login.html')

@csrf_protect
def submit_logar(request):
    if request.POST:
        username= request.POST.get('username')
        passw= request.POST.get('passw')
        user= authenticate(username=username, password=passw)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Usuario ou senha invalidos')
    return redirect('/login/')
