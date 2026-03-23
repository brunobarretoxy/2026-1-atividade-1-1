from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Bruno Barreto Isidio em SO!")