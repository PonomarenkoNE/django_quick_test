from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task1', views.task1, name='task1'),
    path('prodreport/<_id>/', views.prodreport, name='prodreport'),
]