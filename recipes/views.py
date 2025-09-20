from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME1')

def sobre(request):
    return HttpResponse('SOBRE1')

def contato(request):
    return HttpResponse('CONTATO1')
# Create your views here.
