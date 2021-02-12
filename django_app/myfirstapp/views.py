from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductionConsumed, Production

def home(request):
    return render(request, 'index.html')

def task1(request):
    obj = Production.objects.all()
    return render(request, 'task1.html', {'obj': obj})

def prodreport(request, _id):
    obj = Production.objects.get(id=_id)
    return render(request, 'prodreport.html', {'obj': obj})