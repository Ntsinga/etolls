from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def verify(request):
    

    return HttpResponse('Success',content_type='text/plain')
    
