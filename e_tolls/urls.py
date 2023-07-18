from django.urls import path
from . import views

urlpatterns=[
    path('update-message',views.verify,name='index'),
]