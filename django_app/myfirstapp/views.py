from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductionConsumed

def test(request):
    obj = ProductionConsumed.objects.get(consumed=1)
    return HttpResponse(obj.av_price)