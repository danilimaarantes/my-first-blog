from django.shortcuts import render
from django.http import HttpResponse
from core.models import Produto

def index(request):
    return HttpResponse("Oi")

def ola(request, nome):
    return HttpResponse("Ola " + nome)

def dobro(request,numero):
    numero = int(numero)
    dobro = 2 * numero
    context = {'dobro': dobro, 'meunome': 'danielle'}
    return render(request, 'dobro.html', context)
    return HttpResponse ("O dobro de " + numero + "é " + str(int(numero)*2) )

def produto (request,id):
    produto = Produto.objects.get(id=id)
    context = {'produto':produto}
    return render (request,'detalhe.html',context)