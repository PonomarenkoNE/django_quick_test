from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import ProductionConsumed, Production, ProductionProduced, Purchase

def home(request):
    return render(request, 'index.html')

def task1(request):
    obj = Production.objects.all()
    return render(request, 'task1.html', {'obj': obj})

def prodreport(request, _id):
    obj = Production.objects.filter(id=_id)
    purchase = Purchase.objects.all()
    price_dict = dict()
    for el in purchase:
        price_dict.update(
            {el.material.name:
                 Purchase.objects.filter(material=el.material).aggregate(Sum('price_ex_vat'))['price_ex_vat__sum']}
        )
    full_price = Purchase.objects.all().aggregate(Sum('price_ex_vat'))['price_ex_vat__sum']
    produced = ProductionProduced.objects.filter(prod_report__in=obj)
    consumed = ProductionConsumed.objects.filter(produced_consumed__in=produced)
    return render(request, 'prodreport.html', {'obj': obj, 'produced': produced,
                                               'consumed': consumed,'full_price': full_price,
                                               'purchase': purchase, 'price_dict': price_dict})

