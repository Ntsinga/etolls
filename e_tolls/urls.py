from django.urls import path
from django import views

urlpatterns=[
    path('/transactions',views.transactions,name='transactions')
]